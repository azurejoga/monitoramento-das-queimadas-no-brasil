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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95b9b132-5c27-32bd-b382-13f220403585 | -3.34147 | -54.19106 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8b63aae-fee1-372c-ae52-30b280873dca | -4.39412 | -59.91996 | 2024-11-13 05:22:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae8ba9a4-075d-3751-91fb-828e32147d13 | -4.15928 | -50.74786 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a679feb-ff75-3c55-8897-4bbe3cd63f9e | -2.99875 | -51.45641 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4170ff7a-70c1-39e2-88c5-c093ce03efd7 | -4.5641 | -49.38432 | 2024-11-13 05:22:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87ac1a2e-c6db-3fab-9505-585aa21177cc | -3.65759 | -54.65469 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f16458ff-f337-3388-8b20-97907873c661 | -3.49542 | -50.8369 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21e10dac-ba35-39ca-8ff3-16cd676646d8 | -3.05216 | -50.32772 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a642563-3c69-3d8c-93f7-81da3c8f223e | -2.55988 | -54.00127 | 2024-11-13 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c894a7fc-0a2e-333d-bab5-5513e814e453 | -3.96104 | -52.23275 | 2024-11-13 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 026e62f3-6ca2-3772-940a-75abb1bb7872 | -3.85953 | -49.11507 | 2024-11-13 05:22:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f5c33466-8cbd-3218-9426-6c219ee2560d | -2.99102 | -51.03602 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b1880095-d862-3a1c-962b-1d50f9c91985 | -3.0615 | -50.33995 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c92ad6b3-5207-39e4-9a2e-c4fbb07864b5 | -3.05063 | -50.33826 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 131bdde9-8902-3934-a864-1106aaad96c1 | -2.9962 | -51.0368 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3fe602da-f29f-3d26-8dd5-e46e3ee78638 | -3.13739 | -50.4348 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0824f57f-242e-36e0-9771-07f94169f1bc | -3.15858 | -50.59042 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1abc335-4540-38be-97d2-b7f5ea984235 | -3.5796 | -54.64592 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 04203283-6928-3066-b355-8bd604829628 | -3.16294 | -50.44915 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5e8f6e4-88db-3f3b-9ab4-1bfc904add63 | -3.34387 | -48.96027 | 2024-11-13 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b7e58b14-4306-33ae-a0a8-f0c465a0f216 | -2.81564 | -54.7156 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4eb00776-7d32-3d88-b306-c2e4a5be1822 | -3.03439 | -51.099 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15e67fba-7448-3656-b79b-701ca35f1a6d | -3.08578 | -53.26212 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3b072f6-2786-3277-ab81-3d0bf658aaaa | -3.57663 | -54.64525 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 45ee6487-bf68-3f8d-aeb3-03a05e336314 | -3.57552 | -54.64533 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44d1ade2-5dad-3610-8d08-c395c487324c | -3.02637 | -50.97761 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 790fc03e-e72c-3e21-9976-258635f13d86 | -3.14964 | -54.48244 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6ae9f38-4e0b-315b-bb7b-708734d85bf6 | -3.24002 | -50.30483 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6580112a-d138-3252-8ba9-e14d5df570cc | -3.21704 | -50.3835 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b024c6cd-27ec-3a97-9323-dc32aeb0b99e | -3.14907 | -54.48612 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37f4a0cb-e442-3bed-aec3-53be78750614 | -2.9809 | -51.34605 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a82ac65-d51e-3d2a-996c-c500ec9c008f | -4.52146 | -48.93155 | 2024-11-13 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36eaba2f-cf2d-369b-8b48-b3048eed8e1c | -3.23948 | -50.30837 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ce2faca-79f3-3164-b0b3-4c782920ce8f | -2.93519 | -53.22627 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bac5f3d-5594-33d8-85d5-299b236ed6f2 | -3.17104 | -53.64154 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bf86c70-ec1b-3393-b505-406048b2425c | -3.05325 | -50.31102 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f48fcdfd-7f7b-370c-be52-55d7a8295f22 | -3.11648 | -53.70913 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99efedb6-e6d5-35c3-8089-bfedd39ba699 | -2.95082 | -54.20841 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73ff6d90-1d1b-329c-8c30-8f01a532ab6d | -3.77528 | -54.64601 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 507798fc-1eb0-3e13-beaa-6f4452569f55 | -4.6575 | -47.42452 | 2024-11-13 05:22:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 34e02ab8-962a-300e-bb69-59bbae33969f | -2.87239 | -54.20896 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52eeef52-7592-37b0-a719-62b027e4ee76 | -3.13688 | -50.43826 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| efe5ce1f-93a2-3d9d-9c18-d7f22354178b | -4.16251 | -50.75073 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02cb1ca8-f943-3bd0-a279-05052de96ac4 | -3.46145 | -56.31076 | 2024-11-13 05:22:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e4b990a-9fc6-35e9-b0fb-e837df607a9e | -3.10159 | -54.29891 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5e25b39c-abfd-378b-a834-97dc6ca3a939 | -3.02499 | -51.09137 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab96b463-180f-3ecb-b31b-155480a80cc2 | -3.25793 | -54.53225 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4d1eaf9a-163f-3bea-be25-7cddb4445c18 | -2.83513 | -53.3475 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8434f03b-b7ac-3dcc-99b2-f61925719e83 | -3.01939 | -51.09345 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6a81cf6-22c9-3546-9ec2-a9d69c32e0f3 | -2.68504 | -57.37686 | 2024-11-13 05:22:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c056f85a-a546-3ba8-b4af-44e88facadb1 | -2.78761 | -54.03451 | 2024-11-13 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 829a9d79-08fd-30e8-8e20-6dde11198818 | -3.66116 | -54.6587 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 787894f6-fd79-328d-bd37-284d99fbcd84 | -3.20708 | -50.63173 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e91cf3cf-5fb8-3678-a14a-d89f33378963 | -4.52033 | -48.93452 | 2024-11-13 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 19fe7773-0eef-3956-bfac-23205d1e0e41 | -2.36938 | -57.27236 | 2024-11-13 05:22:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 859ada63-1fb3-3da2-978f-43adedf0fb1f | -10.72708 | -49.52436 | 2024-11-13 05:22:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 752c2467-ed94-32e9-bb9c-765776072971 | -3.01154 | -54.12019 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17fb8bb8-d327-3140-af2d-284e551c70c1 | -3.05062 | -50.32819 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 89e6b934-6202-38a5-a687-fdf14b9565b0 | -3.46367 | -59.55508 | 2024-11-13 05:22:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb178c9e-0d5e-3978-9279-f0428485cd72 | -3.04622 | -50.33033 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 31d42a06-861f-33d7-9bf2-dc628d2834eb | -3.23265 | -50.66758 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| afc05920-c29d-3e87-a230-b67aa2ad8cf3 | -3.24388 | -50.31624 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c1f5a8d0-9d7d-38d1-acbf-0b09fe847030 | -3.22466 | -50.29539 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98db6e49-85a4-3e28-aa9f-a89fac366a04 | -3.04899 | -50.33878 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71ed08eb-039e-3864-9676-b17081808a0e | -2.99153 | -51.3444 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c50a4209-3055-3959-be16-3ec9848138d0 | -3.07289 | -50.33815 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3fd438e5-2437-38ba-a7cf-afe9b2d5d669 | -4.51541 | -48.93034 | 2024-11-13 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29dae3b4-9c41-31cb-80ac-cc2185280f3e | -3.98157 | -56.23817 | 2024-11-13 05:22:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04148333-1303-381c-a1f4-d252be584933 | -3.06745 | -50.33733 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 158846ea-7a05-3116-b03c-6a3fd141ef47 | -3.76597 | -54.65215 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6b042d3-ba07-3d9a-98d5-d39b63c93a2e | -3.34939 | -48.95121 | 2024-11-13 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b5969ac9-17d1-3c25-8f7e-776ed38c3696 | -3.92117 | -59.63371 | 2024-11-13 05:22:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1464f037-7491-39fd-b937-3fb526709ee5 | -3.81273 | -52.35163 | 2024-11-13 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17d9ec6f-73ad-3573-b7fa-2a56e17f6647 | -3.04722 | -50.32344 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1e37a2c-478c-3751-8057-662de1515ca4 | -2.77344 | -57.5254 | 2024-11-13 05:22:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 689ef1a4-3f34-3155-858a-fff2f23d08ff | -3.41219 | -54.90228 | 2024-11-13 05:22:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7e0e152-e315-3c54-a9c4-dc159117d50e | -2.97167 | -53.27317 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 400e1ceb-737e-325f-8663-0f554b50b793 | -3.61963 | -54.79432 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24a839b0-764a-329f-bcd9-4e2880d5d1b7 | -3.4363 | -50.30901 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f348966-e475-33fa-877d-0fd846436ff1 | -3.95037 | -48.17447 | 2024-11-13 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a265699d-5ec9-3d83-90ca-407336a2fe45 | -3.48664 | -53.24259 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82a62987-bf79-3151-bcf4-68129d978711 | -3.06484 | -57.30335 | 2024-11-13 05:22:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38377874-a644-3759-8a32-52f39da18fb5 | -10.73344 | -49.52525 | 2024-11-13 05:22:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d613c27-0185-33fd-b884-2c7d3bf63207 | -3.15053 | -59.15517 | 2024-11-13 05:22:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10dce171-3449-3879-a3d0-d0be006033ce | -2.98183 | -51.33993 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 713cc769-bf35-3e2b-88fe-d0af8a9d2d93 | -4.32916 | -50.42299 | 2024-11-13 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1a1de22-cd58-3b96-8018-45d584ebf8e4 | -2.95614 | -54.0892 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 132672f1-67be-33fa-a7c9-1e6fd7dc3423 | -4.52095 | -48.93028 | 2024-11-13 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e020c25-7b96-3ed1-9069-4b7ab677f7fd | -4.56722 | -49.38348 | 2024-11-13 05:22:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56a87c83-8fa7-3647-8271-cd9b53aaa788 | -3.76952 | -54.65623 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6048452-89ca-33be-a328-eff86689d656 | -5.15231 | -48.18457 | 2024-11-13 05:22:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf0d2636-5708-3492-9832-94547da6f8ff | -3.16393 | -50.59122 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f17957be-ece2-3adc-b226-b84ac73b73a1 | -4.16299 | -50.74753 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c93dff88-9f35-3598-9792-b325a9b4b9bb | -2.9864 | -53.97529 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0c7eea66-d122-35b0-8e72-ed95c99da5d1 | -2.72904 | -54.94976 | 2024-11-13 05:22:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fc0765f-da37-362f-8913-b13557b4c48f | -2.93419 | -54.45409 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 581edd74-4c39-3732-b9da-ad794cfedabf | -3.04673 | -50.32685 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8bbfa935-e4ce-3e30-81dc-576cf17747fe | -4.66134 | -47.42889 | 2024-11-13 05:22:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c83e389c-2617-37b9-824b-19606b1d3467 | -4.65385 | -47.43335 | 2024-11-13 05:22:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b08a5aa8-dc0d-30e4-87a2-a7756bc4f2b8 | -3.12457 | -59.01598 | 2024-11-13 05:22:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README49.md)
