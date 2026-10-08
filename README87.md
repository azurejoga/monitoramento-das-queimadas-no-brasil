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
| cdc1a989-7e70-3de1-8417-17e8927f1b24 | -5.48644 | -41.40134 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fcaec8c5-668e-345b-a750-89a1e8f06f9d | -3.52633 | -54.65992 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d1ad3bc-953e-33e1-a143-71ddeef4e722 | -3.31546 | -59.47575 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 892b34bd-aef5-3168-a6ed-23d01c5e27a7 | -6.98735 | -40.03572 | 2026-10-08 04:46:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 920b6fae-8e51-3d30-bc34-a38526269d4d | -3.51882 | -59.32751 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d02b096-ef87-319d-a92e-d8b13e19ecc4 | -3.28716 | -54.00612 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db3173d8-9575-37cd-864f-6a3409400125 | -3.60749 | -54.56441 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bb2b2bf0-4f30-3c32-84b2-3ee1aec4428d | -8.60586 | -45.64573 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e7492ee-3b4a-361b-a76f-6656124e5700 | -3.07495 | -53.94901 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| b7f47355-f43a-30fe-a137-4e98d3b28f92 | -5.8831 | -53.62444 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a430795-188d-3602-a27d-9084eae9fb46 | -2.91088 | -54.10893 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 004ff686-cf80-37b2-87cd-8763ab44756d | -5.73188 | -45.16618 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 09d69bae-c7ac-3750-9553-88338935ad8f | -4.07276 | -59.84629 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 737172e4-6e63-3bcb-b546-56619d0e4798 | -6.32301 | -43.35507 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 475aa265-64cb-38f3-893d-dc07859a02c9 | -3.54409 | -50.09994 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39d3b716-bd0f-3d90-8eac-298bb6a63b4e | -4.17354 | -56.3509 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38180cca-bec6-382e-8bc7-130405423926 | -2.48541 | -56.13458 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b37c39fc-e63d-335b-a5f0-785e6836324c | -3.03222 | -53.93492 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b91526b6-bdbc-3352-b98e-13c9ca877070 | -3.5114 | -54.533 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 297b73ee-a261-3dad-b2f3-1bd07a774b35 | -3.00603 | -54.09952 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e6bf424a-7e35-30e8-99b8-40d548739661 | -3.0925 | -53.71887 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48c67f0a-811a-3fe6-bfc0-ab4f9426b661 | -3.54164 | -53.98709 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e02308d5-eedb-330a-8797-1f73e56e2cb0 | -4.06536 | -59.83421 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c65b8432-2f2c-347d-9360-adfae96cd923 | -3.04279 | -54.15472 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 23ea2415-4149-34e6-9087-39e778a90423 | -3.05024 | -53.91579 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dea8507-d468-3f6f-8222-b45ac91a94a3 | -3.59111 | -55.59275 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d432915-1cdd-3f62-b617-7c05ca1587b2 | -3.18184 | -58.63594 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08807723-2d37-3e00-a2b2-f5f3129bd096 | -2.97684 | -54.0458 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4968f814-3ecc-3f4a-9647-f2553db15f51 | -3.65357 | -55.4608 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 743b2878-d3e7-3198-aeb5-0c32b993a9d2 | -5.23666 | -56.10912 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5b09152-1eb6-35f5-a8bc-cdb18ae9a558 | -9.58466 | -54.63898 | 2026-10-08 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da763c8e-2e43-3f2b-b4e1-4136be8f719b | -3.17733 | -58.63231 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a23a68d-7a1d-34a8-a834-4958809383a1 | -3.26165 | -54.02559 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 920ca454-f17c-3181-8708-1bd7e8b4ed6a | -6.63185 | -43.72544 | 2026-10-08 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cfbf3ed6-72c1-34a9-8932-def0d96a0476 | -2.93538 | -53.93033 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a97f55a-a3ae-3787-b092-4748d047a082 | -9.81379 | -44.78007 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a2a327b-8255-3c9f-acd4-5464934f07bd | -3.17236 | -58.63152 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95605531-4439-307f-9806-e4c1c023edd7 | -3.2766 | -54.05001 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4740a1bd-ec35-324c-a2e5-6dcccc3f231d | -4.52258 | -54.9851 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1999ef0-9175-3901-89e4-164ba8c1ba25 | -3.28694 | -54.07684 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fc46b448-3dfd-3e78-94f3-22f77dc869b1 | -2.72433 | -57.46798 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 776476ca-46cf-3413-936d-8d6140519b1e | -6.903 | -40.91214 | 2026-10-08 04:46:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 15d1fb7f-b016-3256-9207-2e2e0483a708 | -3.93533 | -52.18415 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5f0b1f6-bd02-3662-8d01-dda56438833d | -3.54526 | -54.66297 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 671b6746-9a15-30f7-9b38-8099435afab9 | -5.75261 | -42.05423 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04496a1b-6b4d-3472-9bbf-3f13c1c77b6c | -3.96494 | -56.11562 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf184c21-a1c5-3665-b8d7-c2eab152f055 | -5.62479 | -48.8075 | 2026-10-08 04:46:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa9f3178-83a1-3d1a-9e0c-f068d115cd3e | -2.50392 | -56.1539 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 701c3f21-cb56-3a28-aeb7-38a476cb5f1e | -3.16436 | -54.73369 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8379b83a-a387-3589-9630-14ec9ddd8bdb | -3.04316 | -54.14416 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b430c46-d1ec-319a-b043-13f184f31796 | -11.74381 | -43.64651 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9fead68-9252-3f2e-8afd-84bc9427f410 | -3.27631 | -54.02789 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ca79be3-2954-3f50-8073-469e1d21cedb | -6.10417 | -55.69223 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 631bbbbf-c1d7-37a8-a316-9a02141ecba2 | -3.26189 | -54.04789 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d5c2016-724f-324d-9d5d-c55416a5759a | -3.13633 | -54.35809 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ee0f880-f87a-3d07-95f8-cef2ae7da2bf | -2.76769 | -54.08745 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f99ef9a-d930-3eaa-b9a0-f17399183034 | -3.43065 | -50.43771 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46dec905-c00f-3af4-b912-f07be1f29ced | -3.16358 | -54.73841 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7232f498-4ebe-3589-ae5d-a76a346fe077 | -3.28968 | -50.44322 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c19bdc4-0b0c-38a3-a1a8-ad4c71e32e55 | -2.97451 | -54.13076 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f966b126-4f6b-3dfb-9c7e-a7d35864439a | -4.80616 | -54.67867 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 37c2b457-df47-3105-a7c8-9fe37a872108 | -6.1405 | -47.92528 | 2026-10-08 04:46:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 36205848-b7e5-3600-af34-eb9df1f9041a | -2.78185 | -56.50996 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 757935c6-aabd-3658-97b3-28e9160f27e4 | -5.76227 | -42.06252 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f419214d-9790-38d3-b18d-4cbcd90f0579 | -2.94267 | -54.11661 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 05992914-ae18-365b-935a-9e6516e8ee26 | -3.00374 | -54.09018 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9f63dee1-bf9d-3c72-afa4-35f05638b754 | -7.22147 | -55.08804 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 64d140cc-0284-3cec-bb17-787a679053fb | -3.08523 | -53.95505 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 8f1aaf1a-46f3-335a-a832-f29bb398b8b4 | -2.491 | -56.09939 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9333dff7-53a0-3c7a-bbe0-85e0eb434d08 | -4.06169 | -55.32495 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1efd2c22-e4f7-392a-b78d-7a87f0f9904b | -3.11478 | -53.77264 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e05b9a33-a04f-3720-b96f-ed8d84276f68 | -4.53879 | -55.61342 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56e0156e-d949-3ff0-bf9c-0d5fda0aa5e5 | -4.12381 | -55.02183 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d31751a-193d-3c6e-89e9-5da9d02d50a7 | -2.50185 | -58.0677 | 2026-10-08 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7c3d311-f7c1-39ba-8ce3-08e4602e75f7 | -5.29455 | -60.09291 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8f7ed13-86c1-3d4d-b458-37e750724789 | -8.1769 | -54.72673 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d7be996-d297-31fb-9100-b34341776c81 | -3.51192 | -59.32871 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85493f7c-4338-3f2f-b4b3-1d53249a5aae | -5.96355 | -40.92668 | 2026-10-08 04:46:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 014aafbe-ca5c-32b7-bfcd-6f2ef76eefe4 | -5.69498 | -53.4844 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3aa32ef-d989-3737-a540-089c5a4a380c | -8.23629 | -48.57961 | 2026-10-08 04:46:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 85875132-828c-3d71-8149-2c0ee4ff669f | -9.16528 | -47.57861 | 2026-10-08 04:46:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38397e0d-e78a-3108-be1d-f1ffbab4f337 | -4.8085 | -54.67631 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ffb842ab-d85b-3615-b8c3-a7426ef9432a | -3.32377 | -50.18147 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1461711b-1138-3d12-87a3-696b4961dc81 | -6.98726 | -40.03566 | 2026-10-08 04:46:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ce0cee3a-a0ac-3bb3-9670-4609b384f089 | -3.05227 | -53.90298 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f16281c-8d44-340f-9241-a32b46ef7ada | -9.26743 | -45.63736 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b9ff225c-3948-3c14-8917-0ca4ec981748 | -2.88062 | -54.20385 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| c85ee363-f0c6-3dee-b518-a6737a5d4397 | -8.22184 | -46.3477 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d3fbfb9-0473-3325-99aa-0254bff33b01 | -2.78319 | -54.08538 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a58ec7d0-a203-37c3-8da1-5d34384bd39d | -5.86847 | -52.0566 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f078012-fc75-36cf-a683-1e82b02a6a45 | -2.98123 | -54.04202 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10aa6196-0d30-3b84-a9d6-38dba33360c5 | -3.74164 | -59.44467 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75ea9a29-019d-3974-a0e6-dabda0707683 | -2.843 | -54.12993 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89e411b5-598d-3b0a-a6ba-a2c8fe8d214e | -3.07899 | -54.29971 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02af4ff2-f077-3c75-89bc-493efab2691a | -7.43203 | -63.53776 | 2026-10-08 04:46:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbc5ed9e-5435-37d0-8b79-15380e9fc594 | -3.09365 | -59.19239 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d065d264-33c4-305e-aafa-784219c3293d | -2.7735 | -54.07484 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d59fdc61-037a-3e8e-a749-56b8bbc7e0ae | -6.09636 | -53.49897 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b7470d8-2507-34a4-ae7a-9b33d2ca6023 | -2.99605 | -54.13842 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd553133-c0bf-3411-9e54-6304e6864032 | -11.39133 | -46.67641 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README88.md)
