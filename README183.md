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

## Dados Diários - Página 183

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 718ead78-2ea0-3194-8157-e760703b67de | -3.00064 | -54.07089 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| c714af02-a703-3cab-afa1-74ce9b1bafe6 | -3.05682 | -53.91526 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ab17a7d-5855-352f-b213-c6d2c5c44113 | -3.07958 | -54.25964 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1284f67-bd9c-3536-b4e6-95088ac57339 | -3.29184 | -54.03267 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 525c91e6-9ae3-3935-8d27-6e26159aae86 | -3.06617 | -54.17452 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb7ecdc6-0f75-39d8-b2a8-6e8cf903f0f3 | -2.98412 | -51.24447 | 2026-10-08 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 780637cd-1756-34cf-b0b9-48db65e177af | -3.56877 | -54.36084 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d991d81-720e-3b53-aa80-55027d203ff5 | -7.00124 | -59.11389 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b56e9d7-f903-39c5-8b85-98fff83fe5c9 | -3.05554 | -53.95994 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 28d3f600-15a7-3cd9-b8bb-3631fe126a6d | -2.77311 | -54.08567 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62ec16c9-79e6-39c5-8ba1-93936e504323 | -3.66275 | -60.62936 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 980bd0ba-e810-3bfb-bcd9-fea6b1ad7590 | -3.75799 | -59.47064 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b081564c-75d8-3afa-b17a-0554172d2ff7 | -2.85328 | -59.26666 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc0a301a-9202-36f1-8d8e-5da3ee9512fe | -5.82286 | -53.83306 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ef01021-a830-39bd-8aa5-d1bd8551333f | -3.04325 | -54.1478 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a780a45-64bb-391f-a0b8-3e1c247d32a3 | -3.29824 | -54.67311 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07adfad6-b90c-3b95-811b-1a53641013f3 | -3.30643 | -54.70399 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cb8a5be-43fd-3114-958e-cef7f4af84ba | -3.05247 | -53.90761 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 063f5078-0b98-35c1-8f64-f7b6b1704542 | -3.04198 | -54.25977 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f5f77a9b-ff10-3ccc-8a4e-09eee19702a2 | -4.30073 | -60.95322 | 2026-10-08 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 155462ad-321d-3534-862e-d2cf578be5a9 | -2.99729 | -54.05691 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac769d85-fd81-38b2-a56c-81555c772f0e | -3.84983 | -55.98279 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22c9f49b-b5e9-3c7f-b734-d6b2a7b1f2a1 | -3.51018 | -59.95449 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 013628b5-3065-3346-a802-be4babc988ec | -3.55255 | -59.47049 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e485d74-5d7d-343d-b765-f87904ce029d | -7.23119 | -55.11843 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 287788e3-b028-3926-aff4-b24b5180e2f5 | -3.65594 | -54.2818 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b79a77d-cc94-38c7-8053-a13157479b3e | -7.00474 | -59.11793 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e48f976-f8e2-3a72-b9a0-0f338c2b16d9 | -3.11014 | -53.78284 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8f2f492-8423-31d4-8454-d768e434f27a | -3.53855 | -59.41336 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0480999-b323-3d06-99b9-b63471fadc74 | -3.03053 | -54.08888 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fca7b307-7677-303a-b847-f66d34ce8dbd | -2.50198 | -56.17023 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b7302629-08f5-36f6-81d4-14f21a026780 | -5.88006 | -53.63268 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0214322-08dd-3e69-82c3-4f76a56d0ffe | -3.00623 | -54.14216 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4673ad10-297d-313d-8b29-f74235f86e95 | -3.10682 | -53.76825 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2157d74c-cea8-3b47-a18e-09a39ecfe68d | -3.05469 | -54.20976 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e948d992-8e76-3187-82ab-ed96a4171300 | -2.56726 | -56.17294 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3cda3c1-e8f1-326a-91b8-5dc3cf10b3e2 | -3.01383 | -53.90868 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93a0533c-e881-3aeb-bc7d-54f88518f899 | -3.6024 | -54.56668 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 44fb2222-aed7-3a3f-ad0d-576f8d3e071d | -2.75294 | -54.03893 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92d92de6-e25c-39d9-9030-63b7b5002959 | -3.08234 | -53.96391 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| d938322b-3581-34da-8aa9-7ca8f62f6fc1 | -3.29789 | -54.06441 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73c4f6c1-0f9a-3969-b672-f23573e11af1 | -4.17131 | -56.35163 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87f2d5ee-1bad-30b7-bc22-74440cdc62e8 | -3.19774 | -50.57079 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab9a109f-37d9-3f34-893c-234c17d0a7af | -2.50653 | -56.17096 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| aafe04ab-092c-326b-a3bd-3c53f791fc75 | -5.23918 | -50.90995 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7870e33-1fe4-3684-8f89-e4e903a5efca | -3.28469 | -54.07928 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b99effb3-53e8-381a-88ec-2037e6b24ce2 | -2.76493 | -54.10426 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a91ab4c-a706-3b0e-801a-9d1f731ca118 | -3.10197 | -54.28929 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea275327-3633-35a1-8a3e-4ec8a78204ff | -2.84363 | -57.48283 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43887551-c8db-32be-976c-6c0adf800834 | -3.30121 | -54.02718 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa2d12df-88f6-3cd4-a473-96dd0058f6f2 | -3.01374 | -54.056 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5b0b8af-365b-3480-8593-438c68b6d061 | -3.28977 | -54.04616 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01fd8bbf-dd20-3c04-aac0-cb30133767eb | -2.98709 | -54.08897 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2bb261e1-0ce2-3b34-b7c8-7d60dafe5463 | -3.05299 | -53.9042 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15977b43-37a0-3e2a-a9e5-d9dc3d47c250 | -4.527 | -54.98501 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef1a8751-baf9-3bd6-9a1e-ebf4cc2f134a | -3.09308 | -59.19191 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4e8604cc-60e6-3cbd-b117-8a00e27e4118 | -4.00768 | -56.25856 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32fe9979-3dbf-32c7-8de3-242059c97754 | -2.85055 | -59.10812 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31d6214e-0682-338f-9e6c-7ffc5f6a7ed0 | -3.49629 | -60.21151 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62a66707-96d5-3037-8b70-e7c740232271 | -2.97904 | -54.04288 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b0b715f-0a51-34e8-8b3d-0b3ebbbbf008 | -3.07673 | -54.27876 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de080e8d-1d7c-3d32-96b0-659f29970ec5 | -3.01608 | -54.07663 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9529376-1437-39e8-8005-2c2ee0909efb | -3.30151 | -54.04096 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b35ac741-c577-35ee-a239-5c3ed75db685 | -7.18531 | -52.61908 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25ca4521-c94e-3046-81b7-42f11a15968e | -3.26557 | -54.02545 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 190692f0-d572-399a-ab5e-feb7afebfb5d | -3.59043 | -54.68137 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 92a49f02-5e19-34fd-922d-9ffb6e22bdb7 | -3.02324 | -54.10121 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56eee11b-9a3f-3493-a8b8-ed66d085b96e | -3.17566 | -50.55761 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cef255b6-5e61-3592-ac28-910acd1909b6 | -3.40957 | -58.91277 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c15156c8-c848-33be-aa2d-18e1e074dd83 | -3.44062 | -56.94069 | 2026-10-08 05:42:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25074932-44aa-306d-b60a-4ea89ea61796 | -3.19859 | -50.56501 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 73a29b8a-5c60-3273-a45c-81c99cc5017f | -6.72976 | -55.10794 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a84cfdb-1faa-36bc-b473-2d9670623cef | -3.52233 | -54.66395 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81d91234-fdeb-3fee-9788-39c99011d6dd | -3.16396 | -50.45389 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 97520054-be47-3bb0-9dda-a2acd4a7f681 | -3.69177 | -59.65125 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25456566-a4fa-3e1a-9136-7569dcec72c4 | -3.04607 | -57.48899 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4eb5df2-b5cf-3bb1-9748-26dabd966738 | -3.1695 | -50.59817 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c1dbac7b-5700-3692-95d8-385490a05712 | -3.55061 | -54.66621 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 368e63bb-e63e-3256-a41e-ba28edb0dcc7 | -3.16127 | -50.44491 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 098fbb91-0e75-3dc2-b48d-0bf612bf79d6 | -2.46236 | -56.09243 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f40607a1-1509-3cf3-9411-2dbca13de585 | -2.48701 | -56.11539 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 513f591b-19ce-3dab-9f50-baf3547b592d | -2.89666 | -56.66874 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a0b5b51-b4ac-319e-baf8-001dddec2638 | -3.08529 | -54.29329 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 312617df-98f8-3c31-97c5-bbc96d82ac02 | -2.69699 | -56.54207 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a820068-5fea-3e50-8081-2d6ee23cab46 | -2.47151 | -56.09394 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de21201d-abae-303a-88e1-5649edf56df2 | -4.1198 | -59.883 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1d9e080-291e-3a18-9153-53267900ca5d | -3.13396 | -54.36497 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0dd140f-98de-30c3-86c9-3bdf57fb6390 | -3.47479 | -59.50424 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66832583-b94b-3683-a4ae-aa4ac0a5ed6e | -3.28925 | -54.04953 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e5be920-4043-3538-a047-595ab8165272 | -3.29044 | -54.06347 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99e6be1d-f7ea-36bf-8b1f-d7104350fc80 | -6.99274 | -59.11609 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf99402f-6f48-324e-b879-53eabd84dbda | -3.28316 | -54.03845 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af843a69-a57c-3e73-b40c-9bc28c527df2 | -3.03003 | -54.09218 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ba4f268-d596-307d-b93e-d4513ab9eecb | -3.31376 | -53.86558 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d20ab52-8298-3ebf-9471-4f07a7913bca | -3.31206 | -59.47448 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4715e69-d5cd-32fb-b574-c51fe49dffec | -3.28267 | -54.04182 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45f94fbf-ef16-389e-b39d-e8530b771a55 | -3.29676 | -54.05759 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7740193-4b47-37a7-aab3-4263ec4baee7 | -3.57425 | -54.3605 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45eb1571-edc0-316e-a6d1-b64d193abfd3 | -3.04955 | -51.22416 | 2026-10-08 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 525a23ea-9f96-3948-8a60-273600e72bee | -3.82743 | -55.46453 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README184.md)
