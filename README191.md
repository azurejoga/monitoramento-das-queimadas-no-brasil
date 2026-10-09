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

## Dados Diários - Página 191

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03e4671c-e1b6-33bf-af44-ef54337ba1a9 | -1.60289 | -55.16168 | 2026-10-09 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88f3a6b4-95b9-3a3e-9788-c22eb55525d3 | -3.94363 | -56.02441 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcbe3ff0-6a40-3bf7-a08d-8f2c540e8b51 | -6.4503 | -59.95625 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec66c9be-1907-3356-b204-7bf1b29ec98e | -8.7024 | -62.41094 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94b5348e-9926-3305-afdc-6f092686c78c | -3.25424 | -54.66718 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b0f422d-276f-3b61-ac31-46c7ba59ffa9 | -3.14543 | -58.56118 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cc7c5b7-5691-34b6-8cd2-3e7e91e6be59 | -3.74418 | -59.41148 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8f71a64-665e-34a7-aaa0-ad539f768973 | -3.90112 | -58.96008 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc803c67-cbec-3a4d-b16c-b83c3bd832b1 | -2.22424 | -58.11281 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42928fff-6224-3466-83c1-30a88430c82e | -3.13368 | -54.36552 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4991e510-2bc7-3afc-9d3c-6be0a5459921 | -3.00936 | -54.08574 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ed14c9b-68fc-3a20-beea-cec5e1a4138f | -3.26838 | -54.06577 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3521150a-9b48-3b13-bc4b-07fa43f79db5 | -3.07166 | -59.13352 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de5388f7-b7d4-37ac-bd4b-cdd97e0458f6 | -8.49714 | -62.69275 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae7123a3-875d-35be-a28e-d31a3466737a | -3.16519 | -50.59002 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9c6e32d-8858-3e0e-968c-a2cf5718cebc | -6.99699 | -59.10499 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95a59deb-683a-3708-b216-50f376697742 | -3.41812 | -59.58293 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fd3a507-7043-3400-b369-792afec0b478 | -3.0845 | -54.30879 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ade06a4-0ec6-3da8-9480-6e162cf5b0e2 | -1.53637 | -54.53515 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 611b5c1f-dfce-3c28-9c13-2846167a245e | -3.31072 | -53.70836 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 355a9eb8-d646-354d-b0d0-75d87e8b687a | -2.89211 | -54.17191 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 912870d5-a0e1-33c4-aa71-0649977227c1 | -3.60007 | -61.63578 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34d3b66f-150e-3f51-877e-8de314047475 | -3.11412 | -54.16174 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88d2fad2-7252-3364-ab79-84dc4b2ec84d | -9.27057 | -47.44177 | 2026-10-09 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bfd03400-d37f-3b08-99d5-9d37cdb88e07 | -9.51091 | -64.35245 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5be0bc2e-feb2-3fc7-abd9-be7c5857f022 | -9.20999 | -60.86864 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a66c856-8073-3d54-8b95-9ca897e55e08 | -1.82506 | -55.03575 | 2026-10-09 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19a93844-2050-3d9e-a712-83c91d3ebcb5 | -3.74582 | -59.444 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28a57e88-8b77-3212-ba6b-5d672915a219 | -3.40862 | -59.59952 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a38d85d2-4116-3aa8-b2cb-467598202032 | 0.50673 | -50.77643 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 41a83287-fc4f-3158-9ec2-c09f5fcf79d7 | -3.17825 | -58.63338 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a7df869-f143-3ddf-a8b5-37f9320560c7 | -3.00506 | -54.11427 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a5e66ce2-3625-3064-9d7c-40a2950cdbc8 | -2.58622 | -56.14857 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 905473c8-07cb-3967-8c02-1314edc3b1bc | -3.6683 | -60.60793 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bedcb43f-f730-3234-8426-38ac689ef69c | -3.56426 | -54.68985 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fb47d1ac-0f8e-3d06-bf56-2d5bee28517b | -3.07894 | -54.26987 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a12a462-afad-3e65-8117-91876422ad8f | -8.6918 | -62.40914 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b59ce0b4-98fe-3c46-bd34-7907bc44de1f | -3.48143 | -59.45942 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 621a794f-9492-3b1d-9cb1-fe04fc15a1f5 | -2.9233 | -58.52642 | 2026-10-09 05:23:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65aa131f-4305-3644-a0a3-bd88f9541a2d | -3.4159 | -59.57534 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e639e367-7158-3ca4-83c6-041483e30b8b | -3.00694 | -54.0756 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 824f5a92-092d-313a-8c1d-5fc77aea188d | -6.99644 | -59.10844 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8caac12-d307-3044-ad1a-dbd6bc768503 | -3.10876 | -53.77188 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fda30e6c-0843-39a2-b6ce-e2a82d3cbbb6 | -3.0132 | -54.08634 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83d96a6f-c278-306a-bedb-cc2cfcf87bf6 | -1.83646 | -59.95871 | 2026-10-09 05:23:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 571d3ffa-ef34-3ebb-8db7-333e12e73f57 | -3.60066 | -54.67695 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aae3aa46-b421-38a9-bcec-054af8282177 | -3.00733 | -51.01881 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5303ce6c-8ace-3e23-b6b8-6ed39401ce6b | -2.89572 | -57.19503 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ceb36b9-f593-39b8-ab63-a4a900a5c18e | -11.32249 | -46.65844 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bfca3078-aadb-39e5-a49d-3da691d44c28 | -3.35493 | -50.48066 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4be8426-07bb-3f0b-8632-ed7f6dc58f2e | -7.01639 | -59.11168 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a37d6d2c-4676-30ef-bda9-3a4bb9daef97 | -2.57038 | -57.40667 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97da6873-4ea6-34bc-80ea-408c83f38541 | -3.34207 | -50.40599 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78fcd8fa-af13-330f-ad74-ffa2532c9bd5 | -11.25778 | -46.27063 | 2026-10-09 05:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1f4cd2d-b231-33a3-9238-93b5469df7f5 | -2.57176 | -56.17722 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 007955c0-d015-35e4-a489-3ee42451723e | -3.08951 | -58.01292 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8e9fa3a-38a9-3afc-9811-dc4366906144 | -2.41009 | -56.53382 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbeb7950-c1da-3781-9b2b-47fa34f63c3a | -3.27998 | -54.0675 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b428b841-3d3c-3233-aec0-d0e8b31fa896 | -2.15681 | -58.10917 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78df21c6-70e6-3d94-b521-6350194dd0f9 | -6.94874 | -59.36685 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e65ca829-8fc3-3fe0-8ebe-5dad1706cbee | -1.15353 | -54.22919 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 297ad888-fc9a-36f0-b1c2-306472f52bbe | -3.85183 | -51.93652 | 2026-10-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db570f23-0ebb-3c4a-bbbb-4b2cf0601f79 | -3.58706 | -54.66562 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73201130-2475-3acd-a0dd-34130453f72c | -1.21104 | -55.64934 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6cc15769-681f-32e1-af39-555b5b5ee4c6 | -3.09774 | -53.76506 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74f209b2-02fa-3b3e-ac6a-04767603ca49 | -3.47214 | -60.2579 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 241528ac-9921-3ebe-906d-9c27f1244d97 | -3.45167 | -60.2735 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64d9a53b-da2b-3a2a-ae65-035dea1b1f94 | -3.00236 | -53.88997 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c470319-66b8-35ab-a6f0-9738a7599694 | 2.38829 | -60.25177 | 2026-10-09 05:23:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09ffa527-0197-3982-9ec7-bbded5ae82dd | -3.07857 | -53.96849 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a8728db-d1a4-3bd2-9d05-fb1224ef327a | -3.01064 | -54.75287 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5784581a-331f-30f2-81dd-ade37b0ac155 | -2.879 | -54.16219 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71bb5172-c97d-3d3d-867b-968d25e5eec9 | -2.50814 | -56.15588 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f8c0ff90-6b38-3808-ab83-e8f905885108 | -2.88846 | -54.07693 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9a09acb9-d107-30f3-a02c-7757cace736a | -3.60246 | -60.58222 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6cde35a-bf0a-35c4-b06f-a201d1c42069 | -2.49432 | -56.17672 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6bfc685-ea3d-351e-bc8b-f4d9e7ff7bf4 | -1.12886 | -57.28424 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31a7ab39-83e9-3904-8260-2aae4b05fba0 | -3.01392 | -54.08157 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acb091b8-f37d-3087-99ab-e157774d6ffc | -3.95199 | -56.1092 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c966ae3-1373-3a3a-b2bc-4463327665c3 | -1.18853 | -54.17567 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64087b1f-a5d1-3a5d-bc82-8c4db84020c6 | -2.73384 | -57.46759 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 526c7669-7daa-37a4-987a-58c946ddf453 | -3.6355 | -60.61422 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41a693ac-6264-3b69-abb3-21545ca01d36 | -3.43258 | -60.21782 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f88d1641-711e-3fa1-8039-86a11d65c588 | -1.15421 | -54.22477 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d3e2d79-32fd-3b64-8c04-4c8326e58724 | -2.49515 | -58.07476 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2112ceb-b048-3bc7-9275-861254816ec3 | -3.59392 | -54.56945 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0308b4e9-d2ab-3a40-a714-2d7c9df35785 | -3.8955 | -55.88977 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 22519c25-6a6c-35a0-9269-5182968628b0 | -2.55224 | -58.03772 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f04acc1c-7878-32fe-a20c-e4e4a51d7a55 | -3.51904 | -50.34919 | 2026-10-09 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b4aa34b-beb8-317b-90cc-45ba176991ad | -9.71674 | -46.95043 | 2026-10-09 05:23:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ab188440-2379-3335-8f9b-d2be2b891a50 | -3.55092 | -59.47401 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c85c423-155a-3d1a-8388-5dadc217c072 | -3.01948 | -54.76107 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36476b8d-d3ed-3cb3-94ba-ac629619a140 | -4.63985 | -50.96627 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1332d529-89c2-3536-b092-8dd44a65d4e2 | -3.86299 | -58.64307 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b40e954-1196-3b34-ab0d-34bd089a8d59 | -2.86907 | -59.22984 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d27eaef-3a87-3dad-bfdc-9657fdff786a | -2.98783 | -54.08506 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41c83bf0-a720-3ba4-99df-6d49a7e70914 | -9.22557 | -60.87851 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a3de0ef-fb30-3e6a-b1d7-bdd6729497a6 | -3.26911 | -54.06097 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3730b777-f1a0-3d32-8fe2-445966b663fc | -3.39974 | -59.20698 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f742c8d1-9d4b-3cf6-80c3-b8322664d358 | -3.30051 | -54.01128 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README192.md)
