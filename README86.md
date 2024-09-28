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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ecd9172-aa34-3042-909f-50679bacc676 | -8.81816 | -58.22909 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 32438146-c0c3-33c5-a753-75a434e8c5f4 | -8.81705 | -58.21466 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4156418f-c5a1-3f97-8803-8833570609cd | -8.8165 | -58.21814 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67975bfb-3179-3634-97dd-33bcc6f531d4 | -8.81485 | -58.22857 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec58bdaa-b7ec-3d57-8a8b-22950020c3cf | -8.8143 | -58.23205 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3309a725-c583-3f19-a4fc-b6f0103eb65f | -8.81374 | -58.21413 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97eec459-5476-3c02-84ba-c1e602730602 | -8.81098 | -58.23152 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c364486c-43e5-3249-b8d8-11b701c4bd43 | -8.81043 | -58.235 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d20821c4-d068-3cbd-afa2-18e194bdec4e | -8.81035 | -58.21332 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6caa42e6-fd8a-3b4e-a311-3fd7c25a9c11 | -8.8098 | -58.2168 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ebc32c32-1d22-30e0-a092-d0639e1f478f | -8.80759 | -58.20931 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| a919f363-f67d-3af6-aed9-534e223bd386 | -8.80704 | -58.21279 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d1a7530-8556-341e-867a-80812734d304 | -8.80649 | -58.21627 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d374e399-01f8-3424-9543-728f4fd0cb3d | -8.80427 | -58.20878 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5c789409-447b-3238-a09f-2208abe3ea13 | -8.80372 | -58.21226 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b73c9d71-dbb7-3a46-b400-f068b59eaf37 | -8.80096 | -58.20824 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 05d4e44e-bcef-3886-90d2-331c21530297 | -8.80041 | -58.21173 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee7ca8ac-a8e6-391a-a718-bad65df7943e | -8.79765 | -58.20772 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 795b7d37-ec40-3f4a-a3ae-85f943d36e41 | -8.79048 | -58.23154 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bfe33dc-8401-3b3e-bc30-185deb656f10 | -8.78827 | -58.22405 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f407f45f-c3aa-33d2-a3db-18784b4b10cc | -8.78772 | -58.22754 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8595bf5-4eb4-324b-885e-afd50a326ae1 | -8.78717 | -58.23102 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 227c73eb-ce6b-3e63-9aed-dfc6ef19f51b | -8.78496 | -58.22352 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 362eac9f-28a0-32e1-a39f-63b3986c539f | -8.78441 | -58.227 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc026fca-9768-363e-ac71-72aa497474d6 | -8.78386 | -58.23048 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50e7387a-1e28-3efa-add2-c091130f2990 | -8.74356 | -58.20616 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99173258-cb49-3916-a5c2-3b3dc57a2308 | -8.74301 | -58.20964 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de5e597e-1ebd-3438-8cf6-431b6fe6840c | -8.74024 | -58.20563 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9f0cad2-5dec-3d99-ae0e-7c12809c0687 | -8.68621 | -58.22564 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 482c6ce5-b61f-3395-a700-72bdeb87a589 | -8.68565 | -58.22913 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96079a40-6915-30e9-9b85-5315584af59b | -8.68344 | -58.22163 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5860cd62-eeb0-328c-8add-e2043f06dab4 | -8.68289 | -58.22512 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da045330-2f5b-39e0-a1cf-24e20130b896 | -8.68234 | -58.22859 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90e7a3be-d642-32d6-a150-19bdf9fccf55 | -8.67958 | -58.22459 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 519ceff0-37c3-32fa-b46a-f6e3ec526eb1 | -8.67903 | -58.22807 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c7ccd95-3689-3bb4-b71c-0b78060d6dbb | -8.67848 | -58.23156 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7cedb1f-6945-31d6-a0ee-716e3964b898 | -8.67737 | -58.21709 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e4d0086-5bb4-3a48-91b8-0530e97e0a66 | -8.67682 | -58.22057 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 150afc46-4faf-3828-a5a6-19de2a6c4494 | -8.67627 | -58.22406 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 575c313d-6843-3931-a638-09d6f2ce8aba | -8.67461 | -58.2345 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22fa9d8d-6f80-3665-9061-b04056580ef8 | -8.67406 | -58.21656 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a05abdd6-fa65-311b-97fd-9fecca52e7cd | -8.6735 | -58.22004 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b0cc742-d330-3bbb-b85a-dbf2ec4730ee | -8.67184 | -58.20905 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 725bbeb2-35b8-3281-9459-5b45378b34e8 | -8.67129 | -58.21254 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b06af851-7c01-35c3-82a9-b3c205460f98 | -8.67074 | -58.21603 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc88334e-51f7-3195-9ea1-a95be44a7b25 | -8.67019 | -58.21951 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd0f67c2-9a3a-31b1-b465-db47ad7f6240 | -8.35426 | -58.1762 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f75ef08d-d281-3c60-89fc-3ded93897110 | -8.35371 | -58.17968 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75bc5902-15d8-3dde-abb3-45e96bb8c413 | -8.35095 | -58.17569 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff338e30-4ee8-36ec-bc36-9e994292764e | -8.34985 | -58.18262 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98d1c018-92d6-3b9d-b1a4-4efa5df6b4bb | -8.3493 | -58.18611 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 859ef67c-c9f5-3506-b105-81cf2c74d8dd | -8.34763 | -58.17516 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5ac0dd1-200d-3934-92ef-7b036e4e0663 | -8.34598 | -58.18558 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 549d0cfc-8548-3497-b7a7-47405314b7df | -8.34433 | -58.19607 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eda53e0c-50a4-3cad-bb2f-234dc424bc63 | -8.28561 | -58.76024 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14ea2c8a-6fdf-3005-820c-1d64d588d75e | -8.28505 | -58.76378 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f721d4a5-e443-344e-8641-ec32b5d07faf | -8.28449 | -58.76734 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3aaec63-5df1-3b79-af51-02f43ead1843 | -8.28171 | -58.76324 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1826a660-0c74-32d2-9dcb-84f85ab1856e | -8.28001 | -58.77393 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdf990cd-2859-3167-afe2-336a16f2392f | -8.27945 | -58.77748 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68ad6405-3054-35e5-bfa1-67067545f16a | -8.2761 | -58.77696 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11de6d67-02e1-3ab8-85b9-c9d7a7aaec22 | -8.2744 | -58.78764 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cf50ad8-1322-3e17-890c-801ee0889464 | -8.27275 | -58.77643 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2693e661-2a96-3972-ae42-aff0a22a22af | -8.27219 | -58.77999 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2ec9941-5688-3f13-9e6e-1ae984b9be77 | -8.27162 | -58.78355 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec0ed6a4-4d3f-3363-9211-83307f4d0b74 | -8.27106 | -58.7871 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27b5b013-ae2d-3aa1-87cd-2d8258396c38 | -8.26941 | -58.7759 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e94d34c-0c50-31b4-b730-81c631e1a5b2 | -8.26884 | -58.77946 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8303776e-a316-33d6-a104-9bc77c802d0c | -8.22733 | -58.27048 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 791e10e1-a121-3a36-8de9-1ac45f3df6d3 | -8.22346 | -58.27345 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16f420c8-25c6-34d2-af8a-f55fc74b5d16 | -8.20908 | -58.21395 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36fde3d1-b8e3-3332-997f-6ba03ab190bd | -8.16976 | -58.31155 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9356bb99-c2cb-32fb-aba4-920092079662 | -8.1692 | -58.31506 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1a5316b-7901-3f97-a353-0d2933a6b495 | -8.16864 | -58.31859 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fab0c54d-1d7e-341b-911f-f487bd33402d | -8.15763 | -58.25945 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00d42711-553c-3952-9af2-6a33ee565dc8 | -8.13115 | -58.01893 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2d7cc9a-b9d7-3876-9efd-93b0811d44f5 | -8.13005 | -58.0259 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d02ca885-8fb3-3b42-8b7f-efd496f0811d | -8.12895 | -58.03287 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d32f8ee7-0d40-349b-800d-3d351f9cb4fa | -8.12784 | -58.01841 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 933064b4-73c5-37f3-a698-2adfaea92ca4 | -8.12729 | -58.02189 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fd93772-af56-38d5-b8cc-a8473f166444 | -8.12674 | -58.02538 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55c117c7-23e2-37b0-8c07-1f00c570f7c0 | -8.12343 | -58.02484 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2aa103c9-8c11-3def-9f63-3d7855216046 | -8.12233 | -58.0318 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a120f20b-754e-3bb0-bc1b-56507eb1b1a1 | -8.11957 | -58.0278 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35e45bfe-1341-3d1b-ab45-3b730002347f | -8.11569 | -58.00937 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9989f57-83dd-376b-9743-f7b25dfc0910 | -8.11238 | -58.00885 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b31d641-5399-3741-9b69-a0e224de21be | -8.10852 | -58.0118 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94b377a2-8ee1-3be0-b310-ac403d79b6f6 | -8.10797 | -58.01528 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3bfd406-4c1b-3402-8bfc-8ad2d1cc90c1 | -8.10688 | -58.04362 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 735d2f53-96fd-301a-8efb-4c6de014a0d2 | -8.10412 | -58.03962 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 10903c00-e6a4-3a5a-b173-5f692283337d | -8.10357 | -58.0431 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 06e3a03b-3f5b-3e2e-8a42-6a3ca5f644cc | -8.10246 | -58.02864 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5617cfeb-ff89-3ff2-98bb-d3e192d83122 | -8.10191 | -58.03212 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b8294fe-5e58-3de2-bf8c-202f45f7f373 | -8.10136 | -58.03561 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 83459875-7e3a-3c81-a7bc-3d1a36f99d96 | -8.10081 | -58.03909 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 09203c27-2f61-32d3-aa59-5df5b8507584 | -8.10025 | -58.04257 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d0e4cbf8-d106-302d-8bb9-e7bf88b16d2d | -8.0997 | -58.02464 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c92a5020-4641-3f8e-9395-b9c395d066e3 | -8.09915 | -58.02812 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a250a3b5-a762-319d-8446-8e2b88080a77 | -8.0986 | -58.0316 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 089cb4b9-3a75-36d2-a632-1f98f40f891a | -8.09805 | -58.03509 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README87.md)
