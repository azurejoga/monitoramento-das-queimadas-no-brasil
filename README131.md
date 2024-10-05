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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83444703-d570-305d-8748-9a49b929e64e | -4.28421 | -48.06929 | 2024-10-05 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3ebc587e-c31d-3a08-b87b-8c975faa7d5d | -4.08238 | -47.95036 | 2024-10-05 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 93d4bb4e-b26c-3ca1-aaaa-d836479eb08c | -4.0814 | -47.95732 | 2024-10-05 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 734ac63b-72c3-325a-88c0-09122e60d4a2 | -4.07533 | -47.94915 | 2024-10-05 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 474347cd-6a12-3d30-95a8-0f428a38cd47 | -4.07436 | -47.95609 | 2024-10-05 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 98282053-a15b-35cf-8611-29d98ac39050 | -4.07085 | -47.94739 | 2024-10-05 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 986359d6-651a-38eb-a3b6-fe0cdd2e62d6 | -4.06828 | -47.94788 | 2024-10-05 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ed7541d8-184b-3974-adac-f1f8f4ad20ea | -2.20285 | -48.85096 | 2024-10-05 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 315f74f2-59f2-3d9a-953a-2a6c64e9ed26 | -1.17262 | -48.84851 | 2024-10-05 05:27:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d1ad3d34-3d09-34f7-8641-bdac1a914eac | -1.17181 | -48.85386 | 2024-10-05 05:27:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 088279e3-0ac0-3fb7-88d3-78efd682bbf5 | -1.1715 | -48.84892 | 2024-10-05 05:27:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7fa3d66e-847b-3bd9-90f7-4b7235349299 | -1.17065 | -48.85426 | 2024-10-05 05:27:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 66a2f329-5f89-342a-b90e-22f0f7f41ae8 | -1.16617 | -48.84753 | 2024-10-05 05:27:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2eefcff6-93b8-3dfb-8641-36444abdd795 | -1.16537 | -48.85283 | 2024-10-05 05:27:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 69daf638-4e4c-3162-8d02-8919e890c102 | -1.16504 | -48.84799 | 2024-10-05 05:27:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f84dd9e9-1452-3f76-89d1-4bbe3a830add | -1.1642 | -48.85326 | 2024-10-05 05:27:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 950c0760-d760-3c0d-a243-bd3a126fef1c | -3.31722 | -50.45966 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 343dacfe-7910-30f8-a2a6-0ce921535509 | -3.31657 | -50.46407 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e40adbb-61a3-3824-b0b9-ac53ab4fbf47 | -3.3159 | -50.46863 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 57c3f353-0a40-35b4-bd30-a442e40f24fb | -3.3125 | -50.44991 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4729387f-220d-3fb3-8bf5-26b21de971c8 | -3.31183 | -50.45447 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 082682f9-d35a-373d-bbb2-f3af466f3723 | -3.3112 | -50.45877 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 66fb1b51-5167-3879-861c-571785d592b5 | -3.31057 | -50.4631 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 62c81cb3-119b-346e-a3f9-dd1769b6709a | -3.30991 | -50.46763 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c5aacb21-b356-3a1d-a85d-d0ecffc8c569 | -3.30925 | -50.47212 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| baea9489-e637-350d-97d9-3a65de9688a8 | -3.3065 | -50.44885 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 14dd66e7-aefc-32a2-aeb8-2cb1dbb97f83 | -3.30586 | -50.45327 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c38f35f7-52f7-39eb-8dad-c06a65e428b2 | -3.30521 | -50.45767 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 50fa09d7-9866-3df3-a322-ba4e0813c20c | -3.30457 | -50.46209 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dea162bc-3709-3b62-9e99-a36ab43d3c27 | -3.30391 | -50.46663 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ca0e5004-8e01-3c36-a9a8-5c9ff729e3f3 | -3.30325 | -50.47117 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 920f7719-5b5f-3842-a73d-8d7f3f9d57e8 | -3.29985 | -50.45231 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| add574f9-2b5b-3b5c-95e4-86e068b7165e | -3.2992 | -50.45675 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 16d72beb-3ab2-31c9-90ad-c11424c16572 | -3.29857 | -50.46111 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9188870f-e5c5-3cec-a155-4687b16b965e | -3.29791 | -50.46563 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ed04a7e2-7049-3d91-897b-a0ac66c92a80 | -3.29384 | -50.45135 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd94e650-9947-309e-a9e9-7db1d7c5a43c | -3.29318 | -50.45588 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 371dafac-70eb-3e07-8f61-c15692e4371e | -3.29254 | -50.46028 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f29704a5-8890-3cf5-9054-eabc081f9b7f | -3.28783 | -50.45037 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de81b103-915d-33d4-9952-cdf5a22ad906 | -3.28717 | -50.45497 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f89260ed-0afa-3b07-b122-1cc7f52b7f7a | -3.28181 | -50.44949 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7c66fc7-2806-3817-a807-a9ee8959f41b | -3.24353 | -50.35976 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cc4325ba-1cfe-3580-ad2c-0f8385fc1595 | -3.24286 | -50.3643 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1e6832ec-5688-322d-a431-9fb410fd4646 | -3.24219 | -50.36882 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 30f512ae-2469-3e32-bb25-447b9fc0ee06 | -3.24152 | -50.37333 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e1ba50db-a6e1-3a8e-88e0-45c3b3838eb4 | -3.23683 | -50.36331 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ab469a9-7bce-3c71-b54d-3476bf1ecf6a | -3.23616 | -50.36782 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02541ceb-ac21-3453-9a2d-239d33fe6d4f | -3.2355 | -50.3723 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 07974850-43f5-3251-94f4-d3d78c8becb5 | -2.57529 | -49.07561 | 2024-10-05 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a3923b60-6dd2-30d6-8467-9e3591bdf8d4 | -2.56881 | -49.07458 | 2024-10-05 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c0ff20f7-cea1-32ff-bd5d-103b7165dbcb | -3.98242 | -50.54471 | 2024-10-05 05:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94bf29d6-4f77-39c7-a227-29cd178fd85a | -3.98175 | -50.54923 | 2024-10-05 05:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf9176ac-e427-326a-ac23-5388c8d849a1 | -3.92754 | -50.66833 | 2024-10-05 05:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b316bd97-2c11-3419-a27e-530d095063de | -3.92218 | -49.67887 | 2024-10-05 05:27:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e97ccc5a-6e32-331d-bab4-79af52d8fc7c | -3.9213 | -49.6848 | 2024-10-05 05:27:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27ef4c73-a0c7-335e-b860-b539f1922aa2 | 2.17297 | -50.69557 | 2024-10-05 05:27:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 82a9d573-e2b3-3b71-9092-839d6d430720 | -3.44621 | -50.6642 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ff1637f-3133-3031-a5a1-603aa8b0f034 | -3.44274 | -50.66304 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86672ccb-bb00-3a3c-bb3f-6ebf9c7d3af5 | -3.44026 | -50.66333 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 976a3d48-59e1-342c-bb19-135ccf3da465 | -3.43678 | -50.6622 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7bb4124d-7462-32fb-9af0-ed42d8c8d689 | -3.43613 | -50.66657 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23fbd1c3-5e9e-3478-aef9-b0d15cf95018 | -3.4343 | -50.66249 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61f188a3-7d44-3714-95d1-da2f80bf4300 | -3.43368 | -50.66684 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7386cdba-1b20-3a79-aaec-88ecbf82a072 | -3.29184 | -50.75574 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb9223de-c9f4-3245-a947-0d9ac87bb9b3 | -3.29122 | -50.75997 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c82961b2-fb19-3ac2-b1a3-d2f1513e1867 | -3.23767 | -50.83807 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b3a9d3ca-e34b-39e9-a66f-7d6b9e6676e0 | -3.2324 | -50.83308 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c60a352b-e51a-3a7b-8c71-2bfd4d0515c3 | -3.23179 | -50.8373 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d9703ae0-bdef-3509-aae7-da315a4548ff | -3.22654 | -50.8322 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9716a54-21f7-35d7-8e33-c7f837ee88b2 | -3.22591 | -50.83648 | 2024-10-05 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9560ff62-dd42-3e32-ae45-8f9d53e0db5f | -3.15212 | -51.30543 | 2024-10-05 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64a0ea09-9588-36bb-8707-17cd90c92f3f | -3.14191 | -51.27838 | 2024-10-05 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 611ec597-9980-361b-a35c-e10226f3788f | -3.88987 | -52.17228 | 2024-10-05 05:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b25a1e1-e236-31cf-8a58-4bbfc98d4e85 | -3.84124 | -52.18678 | 2024-10-05 05:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6aee5d4a-c35a-3e71-96d4-3a3999e41d2b | -3.54206 | -53.01998 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebc67e12-575d-3388-bb9e-d7624d73cf2a | -3.54164 | -53.02287 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d911222-4196-3b66-9409-3996aeb90a68 | -3.48246 | -52.83381 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48c9b2a3-1b97-3347-8d7f-288ee0352095 | -3.48202 | -52.83681 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7801cb3d-2588-36bb-b944-c1840ec5e760 | -2.95278 | -52.78044 | 2024-10-05 05:27:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8da38e7b-54c5-3386-bdd7-9649f9c7f1fa | -2.95231 | -52.78362 | 2024-10-05 05:27:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af8abb6f-d805-3093-934b-0c0dfe8afdb3 | -2.95184 | -52.78678 | 2024-10-05 05:27:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bb1b4ab-40e6-341a-a6ac-df07e4201380 | -2.94836 | -52.91567 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51c64d3c-cc21-37a8-a7f7-0c4bb8b7562a | -2.94671 | -52.78606 | 2024-10-05 05:27:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab771762-aaec-3333-9b1f-7e58cb1d3476 | -2.94329 | -52.91482 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 025bd36e-5905-3ada-8b5b-e1f6372ef875 | -2.94284 | -52.91787 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ffaa87b-1c32-3108-a1c0-6b2578ce1ff5 | -2.93869 | -52.91085 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1aa217d9-3ca7-3cab-95a4-6008a4268007 | -2.93822 | -52.91396 | 2024-10-05 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 123cd1e8-048d-3305-ae33-507e64e3f9fa | -3.84677 | -52.35787 | 2024-10-05 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52668cff-a8f6-3087-9012-c6e8e28687a8 | -3.84359 | -52.35522 | 2024-10-05 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6c75efd0-b838-381d-9b24-a5579e7c4d42 | -3.84308 | -52.35865 | 2024-10-05 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 57fc546b-4e37-3873-8c28-2f4eeb78372a | -3.84142 | -52.35706 | 2024-10-05 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53ebef7b-b95e-38a7-a622-dab4918bf41d | -3.84094 | -52.36047 | 2024-10-05 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ccf6b157-cbaf-38a0-84a9-c7ad22351de6 | -3.81138 | -52.38803 | 2024-10-05 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 097fd494-796f-3499-8d6e-2220d59d2004 | -3.72868 | -52.43256 | 2024-10-05 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 28e42642-058e-3c17-8786-8a35adf52b00 | -3.72335 | -52.43186 | 2024-10-05 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdc46958-7c21-323b-9d6c-cf17189ca169 | -1.21171 | -54.52112 | 2024-10-05 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20cbcf75-848d-3b12-bd2d-a2e87860b76b | -1.21103 | -54.52547 | 2024-10-05 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93bd072c-10ec-3c89-88f2-b59cedb4f5cc | -1.1659 | -53.78209 | 2024-10-05 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1075c2cc-feb8-3d32-ad30-694c098779e4 | -1.16513 | -53.78716 | 2024-10-05 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad690530-4c3b-3eab-9757-d569a56b5d92 | -1.16123 | -53.78149 | 2024-10-05 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README132.md)
