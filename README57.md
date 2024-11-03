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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f803b89-b03b-339f-b17a-c9cee4f937e8 | -1.49576 | -54.29355 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e3314cd-3fca-316a-8f1e-ac44c8834aef | -1.48339 | -54.24758 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8249758b-9d33-3921-a952-a4e2e13bc31e | -1.4554 | -54.44626 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1fd4d2f-beef-3175-b6c1-138094c6a3ed | -1.42544 | -54.20069 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 905fdbb4-7b26-3cc3-98d1-6ed374011d4b | -1.42277 | -54.80141 | 2024-11-03 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e7d9f4d-9259-3130-8b53-18352597a991 | -1.42271 | -54.49683 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7aecee5b-0d59-3d44-8ee4-435f3e89565f | -1.4222 | -54.80498 | 2024-11-03 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5620d0ab-d35f-3bc5-921d-8fd9035da69e | -1.41954 | -54.49146 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 958c5d55-f17b-35f7-8055-16afc3242872 | -1.41652 | -54.5367 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 842b8af9-af7c-3151-aea2-9614bc7a5e63 | -1.41645 | -54.78981 | 2024-11-03 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e93c7c1a-dded-311d-b724-a55ea3c7e695 | -1.40717 | -54.54516 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3d92051-fac6-3ac5-8b95-e1dc84524c9c | -1.34349 | -54.61698 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c46b32ec-9e2f-30da-8b52-98200f3a899c | -1.34036 | -54.61128 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aac259db-596e-30ad-bf1e-d969ff81b0ba | -1.3372 | -54.60573 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22132c99-bdc2-3a87-b6e2-9cafaf519832 | -1.33641 | -54.6107 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b84eff4e-31f5-3319-ac41-01f979636dba | -1.32843 | -54.63534 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 76264939-ba94-3abc-9be2-4127b6c059b1 | -1.32763 | -54.64036 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3cc62908-31eb-3f14-8254-d4805343ef0c | -1.32445 | -54.6349 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 568111dd-3e16-3546-ac4e-5805fa8ffb68 | -3.16109 | -54.92487 | 2024-11-03 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8a9ddf7-471e-3ad6-b6b9-33e494d5dbf7 | -3.15684 | -54.46756 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f26f56e3-43f1-39df-83de-7c1798e9d213 | -3.15611 | -54.47218 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90e4dc2f-2c50-3e75-ac00-770a7187c562 | -3.13179 | -54.25974 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dec1bdb6-3b30-31f6-b2f4-1d0b7b639c1a | -3.1295 | -54.25006 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aab521e0-e512-3b9a-9465-9a87c032731d | -3.12877 | -54.25457 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da41f0f6-22e2-349b-b6e9-5dd4adce9799 | -3.12804 | -54.2591 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 265665d6-c076-3b16-a0f9-2e4304d94dcb | -3.12574 | -54.24943 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| efbdbc56-183e-3ad3-9457-f9077e287644 | -3.12501 | -54.25394 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eab34cfe-a1dc-33b3-b3ae-a520d0ebb589 | -3.12428 | -54.25846 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03e81d83-6619-3fe0-9bf2-e98c8ef393e4 | -3.12355 | -54.26297 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf568b43-0193-3d05-9fd1-f5de6643fcda | -3.12199 | -54.24881 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| db1719d0-0134-3761-b7d6-eaa8834735df | -3.12126 | -54.25331 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5828266c-1493-3d65-b01b-47d371180ba9 | -3.12053 | -54.25783 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c56ba63-705f-39c9-a18d-740d4639bd22 | -3.12033 | -54.47601 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c45d1b33-41f7-3eea-98b6-5097a07322ec | -3.11979 | -54.26234 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bad175b4-c155-32ed-8e5b-eeb7df2224cd | -3.11906 | -54.26687 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abf24d04-83b2-32a1-8d46-1b1b76666a51 | -3.11833 | -54.2714 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88cd6e10-7942-36ad-82ba-627a6a43014b | -3.1175 | -54.25271 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bcd65449-8808-3192-baf3-5a2b476ee82b | -3.11676 | -54.25723 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50e324ae-ec51-3b67-b4f8-6bea77cc296c | -3.11603 | -54.26175 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef1eec89-81b8-3bb8-9150-b39e870310fa | -3.1153 | -54.26628 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0947884-9333-31d3-bfe6-c6714fbb3b8e | -3.11463 | -54.29424 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60029ea2-6d09-3eca-85d3-66bee531d60f | -3.11085 | -54.29366 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac91b181-73d0-307d-b692-bd5486f3bd62 | -3.10886 | -54.47439 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4b863c4-00cb-3eaa-90f9-9f046a57259b | -3.1081 | -54.47914 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec55f204-5d5b-3fbd-996a-b5c68e628cbe | -3.10782 | -54.2885 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7d2af19-c1b6-3ce3-81e3-31f56a5c6767 | -3.10708 | -54.29307 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4ce0604-34f2-31a9-ae5c-e0b083944afd | -3.10504 | -54.47382 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 85f891dd-f132-329f-94e1-79a09ddedaba | -3.10479 | -54.28334 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78602f38-9215-3d1c-b6f3-cfc91ca253c0 | -3.10405 | -54.28792 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c509fff9-0b96-3e5a-9dd9-768c1debd136 | -3.1035 | -54.28893 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cd035b9-1112-3051-85d0-2d8bc8738d48 | -3.1033 | -54.29249 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| daee02a5-061a-3093-9f01-0c7f7e6cf114 | -3.10028 | -54.28733 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1004b529-372f-3bd2-a807-0f1ef169bc38 | -3.09973 | -54.28833 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66b577f9-e9de-332b-a2e0-1b0084fe0759 | -3.09953 | -54.2919 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c4f5743-a78f-3e5d-9560-be1a3ef28dfa | -3.04423 | -54.20033 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7d26fda-2cdf-3217-981e-e90c2df39dc0 | -3.04351 | -54.20485 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 420d2fb5-3646-351e-9920-1b0654b8cd79 | -3.04048 | -54.19974 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45e32271-5785-359f-9eb0-77f6f6f527f9 | -3.03975 | -54.20427 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55622e6e-d81e-3697-834b-ffbe15393b22 | -3.03672 | -54.19915 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 398d7bcf-cad7-3ece-8d69-b06df3a955ba | -3.036 | -54.20368 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3229b83f-adee-3c19-ab10-04c95f24a9e9 | -3.03297 | -54.19856 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 718be190-7328-3843-bab0-00acc6bddf57 | -3.02921 | -54.19797 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0fcf95b3-fd4a-3314-a2f7-70ed0ce1294e | -3.02875 | -54.4919 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fabd2e37-9208-382b-954e-30e9433a80fa | -3.02848 | -54.20249 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b37c9b17-4991-3068-aba8-fdfe7c2b2283 | -3.02798 | -54.49672 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e707c0d-87d8-3b24-91c9-24889d3a86bd | -2.98283 | -54.55797 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bef7513d-5363-32c5-8b22-26658329fcf3 | -2.97899 | -54.55741 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50ccbb16-4588-3a79-acb0-4f3be5fa5d12 | -3.33864 | -54.17453 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6038b670-e09f-3450-844f-76339d53e013 | -3.33768 | -53.79708 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9bf756c-0fa6-33fb-b83d-77dab8191539 | -3.33667 | -54.17228 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78c3c810-d7e7-39ed-ad9c-bf933b353c09 | -3.33592 | -54.17687 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a25b6249-6c38-3c5d-a982-7c0a50c1170f | -3.33536 | -53.78808 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5813bcc-9621-3592-8d1b-5b1e7d1b52ff | -3.33491 | -54.17392 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 900be697-0bec-31a7-9937-f447b7ae83a4 | -3.33469 | -53.79229 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6a14c35-e981-3246-b9c7-979303c93dc8 | -3.33171 | -53.7875 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bc560187-998c-33f8-a400-fd9cabc132d8 | -3.33104 | -53.79169 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d71059b9-9dce-3c40-9ad5-9ef3cd30f51b | -3.33037 | -53.79589 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a6d770e-b862-3147-b518-090f11f350e8 | -3.31001 | -54.1377 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5f651af-0c83-3f62-a795-334be47ba4be | -3.30697 | -54.13276 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0688ea55-f741-3c34-b82a-475336d77708 | -3.30393 | -54.12781 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9bf2873-bfc8-317b-a131-c0f0516d3928 | -3.28672 | -54.52607 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76fae1cb-c68f-3a3a-aee4-b4d893b43dd9 | -3.28596 | -54.53071 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b30e6c6e-1518-397d-ad07-f0a6778ef47f | -3.28268 | -54.53248 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20e006c7-21a7-3e63-8402-0bb09ef1e2ef | -3.28194 | -54.53717 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7558c63a-fec8-3f74-977d-dc473a01df65 | -3.28139 | -54.53476 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cac0938d-e667-30c7-b151-43df18954709 | -3.27813 | -54.53656 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c251c23-cc5e-38a9-b2a2-33f8e0b6a395 | -3.27757 | -54.53418 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c43a474-7444-3ed6-9af0-3bf60317adb5 | -3.27719 | -54.77926 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ac10e9e-4275-388d-90e3-d3e439b3aefc | -3.27679 | -54.53889 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a389aaa-e312-35a7-bf14-706f0ae68de8 | -3.27429 | -54.53605 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ba358e4-accf-33b3-83cf-5071f10928d7 | -3.27296 | -54.53838 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5b611ad-aa20-39cd-b2be-eef27a791a35 | -3.26995 | -54.1729 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc8deaeb-b62d-398c-9a13-eb5f2a686e6f | -3.26924 | -54.17736 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4439351e-57e0-3ae3-b5d4-1f78a2ff4e81 | -3.26662 | -53.74801 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcbb74da-7c3c-3a69-b4ce-49371d375813 | -3.26593 | -53.75235 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe50bf75-e471-3211-844b-6643f9912d78 | -3.2655 | -54.17676 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16136fbe-501b-35bf-85af-19b22ba3aa15 | -3.26297 | -53.74743 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01a7636c-6605-3b44-bfba-160efb745a2f | -3.26228 | -53.75175 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7c4097f-5e38-3593-835a-05d572bd7fcd | -3.2616 | -53.75609 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd6ecd86-f07c-33ea-b190-ec4363730f09 | -3.25795 | -53.75548 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README58.md)
