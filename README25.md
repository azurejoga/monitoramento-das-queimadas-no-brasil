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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bbf721c-6c2e-3578-90ec-0df81fbaed1a | -2.81091 | -48.6614 | 2026-10-04 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4fe4325-7650-3c2c-b5d4-9bf2bb373f69 | -3.71303 | -50.6612 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2140ec89-5929-3d39-aa90-3e9162defc2e | -2.97353 | -54.09245 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70231e28-87bc-362a-a0db-becd6cc60127 | -2.95357 | -54.12155 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4de1a6f1-0f2e-3f0c-8b4c-cb9401628298 | -3.22772 | -54.30941 | 2026-10-04 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33bb75c9-814d-360c-a509-ece794899592 | -4.27543 | -42.11293 | 2026-10-04 04:19:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a349fc6e-7479-35ed-bb33-74c9613fe466 | -4.98235 | -46.0378 | 2026-10-04 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f235e734-9b5d-3349-9c2b-5ec2a0618a17 | -3.86908 | -55.81357 | 2026-10-04 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| a6e08583-8a74-37c4-bd07-5e4e8badb121 | -1.8781 | -50.61793 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 386a4aab-19d9-39ca-9a1a-64afd84785f1 | -3.20949 | -50.75211 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4e9fe86c-bd0c-36b1-bcfe-16d3281dbf7f | -3.92696 | -40.74261 | 2026-10-04 04:19:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2369fa60-da01-3330-ba41-524a9273c284 | -2.88698 | -54.13813 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cbac658-3da5-37d5-906a-2b79f0b6e27a | -4.33304 | -46.64953 | 2026-10-04 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a100b9d8-3189-3bc1-ac30-b3e43a4b1390 | -3.5123 | -54.60504 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0cd92a5f-2344-3cc6-a246-da2e56f40555 | -4.27696 | -50.26451 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f4faaa2-70da-379b-b5a0-e7ec96ed8edb | -2.80585 | -54.11951 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fc9ae916-eca9-3b4e-8214-2850f0038af5 | -2.90025 | -54.12835 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f63efe0-7f9d-3dc1-aeb8-c178194820fd | -6.8656 | -46.41617 | 2026-10-04 04:19:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f943da1-f168-3fd1-a2f5-b9381b34be68 | -3.29964 | -53.84442 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56683b48-8de0-349d-810e-44b910a0461d | -2.79016 | -54.1092 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b9e8e0c-8ab0-393c-a2d2-4a3083cd8c01 | -2.25424 | -51.93176 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3f48cc3-2416-3175-88a9-2d2241550021 | -3.46661 | -50.09766 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c603023b-29a2-30b7-93d1-0514c4a08aa3 | -2.25255 | -51.92968 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0dcf6380-2f8e-316d-b305-928bd6aa2cf0 | -3.08265 | -49.53029 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2d0944a-71ea-3d15-a6cb-986e7b58a892 | -3.01983 | -53.8924 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 794a5b7a-f776-3039-80a1-324e63e4f855 | -4.25858 | -46.36916 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2314899a-40c9-373f-85ec-3db616a62dc4 | -4.26943 | -46.36706 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 9759073c-c7be-3258-a2dc-5de53dbfe789 | -0.33415 | -52.03799 | 2026-10-04 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7e7c6d1-4b41-3c78-b40e-3c11889990af | -3.12342 | -53.74431 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61441789-cf3c-33ac-804b-c29f8fcae66b | -5.04252 | -44.4659 | 2026-10-04 04:19:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bea6bb62-a951-3be4-a786-186fb2face9c | -3.5058 | -52.95785 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad6d2cc4-1380-3041-9c6b-e2e479f5c073 | -2.57951 | -51.87957 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ba33e8bc-05d4-3747-a8ac-318f7475db27 | -4.13024 | -54.1632 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c01c363b-6d82-3195-b966-4431e475ee01 | -3.17461 | -54.08579 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd99f36a-37e6-3171-bac3-19ba63e51646 | -6.31519 | -43.34181 | 2026-10-04 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8bf21e6a-2713-3f2b-9eeb-b7b42d1ddeee | -3.30435 | -48.89415 | 2026-10-04 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caa6740f-9e7e-3286-ad58-23c0c3dd5060 | -5.73719 | -44.83312 | 2026-10-04 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1045cb4-60f1-3f75-a3e5-1359df38406b | -4.48345 | -45.5371 | 2026-10-04 04:19:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 783ced06-7ca6-34a2-82e5-4af9be803e3f | -2.98118 | -54.09435 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bbed084f-4edd-3954-868b-3f39ebc6506b | -2.80778 | -54.10799 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ebd2272c-5d6d-3b1b-9095-12c29991e7b2 | -6.06548 | -53.47483 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6546e39a-e881-374e-bb5d-241217685c3b | -3.07898 | -49.55249 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c84d0d33-bd00-3663-9e3b-b352fa4514a0 | -3.11609 | -50.27742 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3dd7563-6232-3dd3-b8bc-330a23dda789 | -5.55101 | -44.21439 | 2026-10-04 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aba73385-50cb-3e52-a2ff-636390c5236f | -1.09947 | -54.11427 | 2026-10-04 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aa1db8c7-19b5-36ec-a997-e8f8a8cba940 | -5.86649 | -55.70429 | 2026-10-04 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e853e980-86f5-38ce-9446-afc538da7f9f | -4.84507 | -45.98656 | 2026-10-04 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52d87f08-067c-3395-8299-3898178d0522 | -2.92902 | -54.1647 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02c40020-f79c-3a39-83bc-4e0bf2eb8fdd | -2.48767 | -56.09058 | 2026-10-04 04:19:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5d1c6fdb-77d1-384a-8fae-fbdc6ab24654 | -2.82152 | -54.13006 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| af270f15-0f53-3058-8ce0-14f03e6fc7d4 | -2.86176 | -49.62966 | 2026-10-04 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 806cc973-7967-3f0e-a6ca-1ad53c23d94f | -2.9785 | -54.09716 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cfadcda0-a4f2-3942-9952-b89ecf73e123 | -3.06556 | -49.53929 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 293446a9-106d-36ca-a018-ec223cd959f4 | -2.24763 | -51.92887 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60d588d0-fec1-3f69-8d98-0aaf54430e23 | -5.74257 | -45.14449 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7638e46e-fa73-3afa-b29e-66642a6cee07 | -4.28839 | -50.27446 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4ca3c10d-7931-36d4-be3f-45d47568e1d5 | -2.44175 | -49.02865 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79517022-3648-3908-b85e-dc9f1be53893 | -5.80882 | -50.12883 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8665f6d5-f16a-3b2b-bdd0-612d3508b9d5 | -4.2897 | -50.26658 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 7fc97de4-94b0-3ea7-9585-864820abe61f | -7.013 | -47.52459 | 2026-10-04 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| caf5fb5e-90bd-34c6-af73-fbfaa9227df5 | -3.18708 | -50.53488 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 934cdeb2-3c88-39b5-86af-5c76401a3e5e | -3.12773 | -53.75238 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c7db916-3772-36a7-ba58-4e3dd9135a53 | -3.11853 | -53.73981 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a16cc8a0-ab1e-3842-a875-f21af48f1cb7 | -3.28371 | -53.8382 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc547e93-df29-3d37-9c38-71eea27209e2 | -4.27989 | -50.27308 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| ac3a9e61-c677-3a93-bc7f-71c8571df115 | -6.35659 | -45.61477 | 2026-10-04 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9a94ed34-d133-3bd5-be34-80be08320435 | -3.50707 | -52.95926 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 705ff13a-f090-322e-93f9-cc2a4fa4c009 | -2.36218 | -50.60302 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff5e8e86-0086-340d-9d88-74dee7edf48b | -3.28922 | -53.83904 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80c4bcf4-7586-3071-a29c-29b64f43b0bb | -3.12697 | -53.72276 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6f91da04-dc9c-34ff-8872-b0f3ab08a6d0 | -3.18455 | -54.09538 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 429c417e-41ec-3cbc-9291-831c32932428 | -3.51029 | -54.61705 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a13a30a5-4668-3333-8df0-5fbc0d0b9b8a | -6.00236 | -53.52263 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 09782585-8c44-3b62-8b9c-92a1bc6b3dae | -2.80406 | -54.09558 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 117703de-4972-3242-bcda-56bee8495929 | -2.97532 | -53.26813 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efbaf78d-f5a7-3ed9-9897-41289507af44 | -2.91731 | -54.09577 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 759247c3-0ded-33f2-b2a4-70740208ab35 | -2.22221 | -53.7128 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 880f9de3-3d11-3344-b711-b2fe1b9b8a6a | -6.0598 | -53.47707 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39bb97c2-0395-3636-b4a6-fc933eaf9358 | -6.0039 | -53.52398 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e100b05a-981c-3e7e-960b-f97b6429b5df | -2.97058 | -53.26366 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6aaf9a63-7c8f-3843-b124-17d23d6e4276 | -3.19376 | -54.09852 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4fff782e-d23c-3335-9ec6-3259be7788fc | -3.07959 | -49.54879 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e7308f9-e15b-3e8e-a9df-088d8fb49de0 | -6.61235 | -41.55666 | 2026-10-04 04:19:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b4ce5c7b-4d91-31d3-bc7a-77674c7307a0 | -5.78004 | -50.20777 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7489fe7-219b-32bf-a3a9-dac522451802 | -6.06673 | -43.52011 | 2026-10-04 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d0d6a9d-bd1c-3308-a182-68028f2f5ae1 | -3.19194 | -54.08545 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e4259f80-a7ad-37d6-ab9e-101b994631d5 | -3.12832 | -53.7488 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d2dff75-6824-3667-8021-9b0fb35592c5 | -3.70424 | -50.65969 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b2e0cc5c-2b22-3066-876a-cc341b5875da | -2.82719 | -54.13094 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ae7ae539-f2c9-3f39-bd33-672b863049d8 | -1.09365 | -54.1134 | 2026-10-04 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58b86262-1190-308a-ad7d-e45e99a2c2c5 | -4.2608 | -46.3772 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f0b58b02-cd33-3c56-948a-684cfd96ec85 | -2.82212 | -50.5033 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10466164-e858-302a-8ada-c4d1a7357c6b | -3.47446 | -50.10302 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5c457cfb-a751-3181-8b8d-864fa654a523 | -5.99896 | -53.64293 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ac4d491-2ce6-3da4-be16-d74b781ce169 | -3.08381 | -49.53077 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 484b88e7-7d96-384d-99bf-8c0b6a7214e9 | -3.00944 | -53.88282 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2685657e-ceb5-3864-87ce-986c979df677 | -3.11972 | -53.73262 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 928983a8-c417-3064-8058-39818846d89f | -3.11482 | -53.7282 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| dfcbd0e4-3cd9-35c9-9099-ed62274254b6 | -4.80373 | -48.22316 | 2026-10-04 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2e7d4ca-d221-3416-9a40-a6f62a251e86 | -3.27561 | -53.81912 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README26.md)
