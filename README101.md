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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b708c6e2-27bd-3857-a475-13400f709783 | -3.38445 | -51.66503 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 579cdfb1-21fe-37d3-a06f-84ebfa2a0a6e | -3.89034 | -55.88158 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d523c49e-b8cb-384f-9ab0-bd76efcf2338 | -2.7756 | -54.0617 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d279795-e208-34ab-a4f6-ed0381e1d6bc | -11.62988 | -43.69841 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5536a751-c0dc-39cc-9792-0c0aee160ae8 | -3.89768 | -59.44495 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1d2302f-3e67-3fc7-99a3-690ba0579e7c | -3.55282 | -54.66421 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e73f4d6d-21e1-3181-8280-d1e20913c8e5 | -2.7854 | -56.50186 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fd07015-8d33-3b47-a270-09bcd1b60eb1 | -3.83649 | -55.98434 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 050fcc24-0272-3ae1-9f84-988eb946afa1 | -3.28906 | -54.06382 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c681f29-aec3-318b-a0f1-1d6bb4debb68 | -3.29604 | -54.02079 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3e5e09e-490c-3895-a2aa-fbf3613a8510 | -7.89808 | -54.71684 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 791c00f7-fd1f-3525-a5b0-008210c8f542 | -4.15622 | -54.91948 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c6094c13-83ac-36c4-a76d-6ee5a6ff08c8 | -2.49864 | -56.16074 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 348434a8-5ce1-3232-96b5-57b0f295c330 | -5.23529 | -56.01042 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cfe12ef-73b9-3820-a04d-6495fa6bdd8d | -3.72528 | -55.97454 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3d90f27-29a5-3961-9697-281c938c1ed3 | -2.49658 | -56.06424 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b92a8ad2-2ec7-3c27-980d-0fe948e16d18 | -10.24454 | -49.6526 | 2026-10-08 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d1c5e18-6d4f-3d79-a753-a6a454100827 | -5.90115 | -52.04376 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bf4cd0e-0911-3602-aacd-148be391713f | -3.00005 | -54.08961 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7e7e4a4d-6145-3bfe-9d32-7a49e69514c4 | -3.26029 | -54.03422 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c2e5a315-ff3a-3306-803c-fab697bb3619 | -9.89919 | -44.80309 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a1a1257-0181-36bb-9913-a3014c82788e | -10.24106 | -49.65207 | 2026-10-08 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6de34495-0084-342a-b52f-bf532e030a63 | -3.2957 | -54.06929 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35825897-8a1c-3c8e-a679-8463d29f36ee | -2.94375 | -54.18009 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 768710f0-aabb-3cbc-bc21-afbbb25597c8 | -4.63883 | -48.85765 | 2026-10-08 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 805d1e42-1bfa-3dde-a25b-a2314a43fc82 | -7.60494 | -46.76255 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12dcca14-0c4f-37fd-a595-070be4b299d7 | -4.45321 | -47.92429 | 2026-10-08 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ffdc6ea5-caec-3e44-bc32-f206985e77c8 | -3.97672 | -56.12133 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd9aef95-9ef9-344e-bcfc-a34c733b6aac | -4.43114 | -55.1614 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a86b4ee1-7275-3fd1-b8a3-66c562379e6f | -6.09573 | -53.50283 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb86bb0c-991f-3459-b435-ae0428dbc009 | -3.19139 | -53.94897 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2981a029-dadd-3b0a-b032-90be52477543 | -5.73012 | -45.15546 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ace8f7ba-a077-390b-b1fe-6eb35c4af72c | -3.53338 | -59.49572 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfe73e7d-ad6f-36c4-841c-1ae0af3560ef | -3.0598 | -54.20544 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c0eb1e4-fd30-3e70-8527-08c277e2d843 | -7.39818 | -44.47522 | 2026-10-08 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32c4dd81-c09a-3a89-8e96-804bf2818aa5 | -7.89162 | -55.00639 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76f9564b-1980-396b-b1e0-4c180190fdaf | -3.61843 | -55.27978 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95416975-20ed-3197-8b8c-02bfa6440920 | -2.99955 | -54.11644 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b407354d-0279-35ae-a3eb-004da15bcb6a | -2.95518 | -54.1096 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4b29bb2-20ad-37b0-861f-1e5e877bd847 | -7.34271 | -45.28953 | 2026-10-08 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ef5e244-7317-3b3c-9123-661760fabb96 | -2.76328 | -54.0913 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b12203a-e543-3e67-998c-51f604de7bc1 | -2.98177 | -54.1092 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0286898e-b60a-366b-a480-0218eedb87c8 | -2.5759 | -56.16514 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6d85dea-b17c-36a8-80da-56458c636d01 | -2.51111 | -56.16299 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 484ebe6e-94e5-3c81-89ee-72648dba68e5 | -5.74156 | -53.4604 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d7e380f-8ea5-39ce-b687-84ef09395fab | -3.53998 | -54.67154 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 32825fda-762a-3b42-b233-4c616c1cf102 | -4.11726 | -59.87409 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61195cf9-459f-3a87-b01e-a5c7e8176642 | -3.27428 | -54.04081 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d098deb4-1053-373b-96f0-6436f4cdf94d | -2.94349 | -54.11856 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 672d2a2c-cefe-3939-90a1-cbf0968363b7 | -3.13186 | -54.36197 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1883723-082f-3738-be99-0ffe404ccefe | -6.46238 | -55.47672 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ef352b8-34fb-3289-b7be-78f65505a7d0 | -3.09748 | -54.27963 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 43a4fd20-6aca-3c2e-abb2-1034740bf862 | -3.07424 | -57.75138 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 80fe1b1b-1340-3d2b-bb85-5fa7e098643a | -2.50519 | -56.14617 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d68cb4c9-88e8-382b-a0c4-d1bc09917a4f | -4.4616 | -54.97559 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c53c0a0-c52a-3b09-beb3-b71d0d989cbf | -3.08115 | -54.28622 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ae237251-32c8-336d-83ce-56af5211aa21 | -5.83357 | -51.99726 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e952a7d-9ce9-3b11-8a92-b8bc478eb577 | -10.46181 | -47.24337 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb0a45dd-2351-375b-9e9d-9b45329723f5 | -3.85718 | -52.03299 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96abcd7b-d9ed-3396-8a05-f1b888727731 | -4.54158 | -54.98844 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ed25a55-800d-3414-959a-af5cdd03beff | -3.26436 | -54.0084 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f63fb122-b081-3f53-b3db-3086aa5418b7 | -3.71624 | -59.33321 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ed7863b2-0a48-3d91-927c-9537200d1c6d | -4.28809 | -49.09003 | 2026-10-08 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9bd2430-b68f-3aec-a12b-43dd89ef9044 | -3.84118 | -55.98128 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b82c3b1c-fc32-3617-aae0-b3e1048d1fbf | -6.47966 | -55.30177 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 071739c2-92e2-36c2-a507-05f6db3def92 | -5.82408 | -53.8326 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0701baad-b099-3a23-9508-b2165646eea2 | -11.71593 | -43.65892 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b65bf0c9-d118-323f-a805-5a9f86bcf7ff | -10.44595 | -46.8508 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81059fe2-d41e-3059-8d14-c4460e41af04 | -5.34212 | -48.56634 | 2026-10-08 04:46:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 283b721f-07d1-3433-8349-bf2d009755a0 | -2.94708 | -54.1128 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1e98d7c-7577-353b-ade5-b217a1752f58 | -3.1193 | -53.79063 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 44379b56-6a2a-3d80-bd93-1758dfdf7327 | -5.89614 | -53.4997 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 503eb69f-abdc-3987-ba7c-ab560fd5d799 | -3.27089 | -54.06242 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6261d35f-c9ac-3a84-b76e-ae340d21403f | -2.48791 | -56.11889 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb3ba886-8574-3fe4-9e84-29ed3511b8d5 | -2.84684 | -59.11292 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c82b45c-0148-37ef-9a59-7dcc8f889b6d | -2.46632 | -56.0914 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73f20bb6-ccee-3a33-9a58-870d081abe27 | -4.51699 | -54.89851 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fce6d061-31ce-3ad0-b554-256fcbf627d2 | -2.49139 | -56.15163 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69b6f240-66e6-3d44-9f3f-13ae553822e3 | -11.63544 | -43.6959 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fb22438b-55e9-3bdc-b5d7-0632a669f907 | -2.76344 | -54.11394 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 44faa45e-6f29-33ee-bedc-0fef1947de1b | -6.16091 | -39.433 | 2026-10-08 04:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fc1bb6b7-456b-3452-a647-7957fb2e1530 | -3.79468 | -50.87411 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b5c1272-1a94-3c12-9755-79cf9605d59b | -3.01064 | -54.11818 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| c8f13d65-34aa-3e14-a1fd-abbb778ff207 | -2.88708 | -59.2001 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9821bf5-b0c0-3529-946a-b03631813cf8 | -3.51801 | -54.6633 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1740cbc5-8249-3fc2-8126-ce258d971f40 | -6.08984 | -55.73047 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d4ce35d1-3337-3f75-b25b-90e905a44397 | -9.40274 | -49.00752 | 2026-10-08 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3522787b-09b9-30d5-a4b2-d8b3f8c4dba4 | -3.58617 | -54.67427 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 67cef94e-8d95-30b9-ab2e-388a6501f756 | -3.01711 | -54.10124 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 9c21140e-01b2-3b13-a66f-7001c6672968 | -3.7359 | -59.44699 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4736ad5f-2c18-3c69-9d55-e8db8a1cc163 | -3.83357 | -55.97631 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cc107e3-b17b-33c6-b0f0-91ea8ec1ed39 | -3.01101 | -54.2359 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fa01498-0f78-33e9-9afb-1e3effa4b369 | -5.74302 | -45.05611 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a4f3d9f-71ee-3458-9053-60b659ffaf63 | -8.7289 | -45.17826 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c82f985d-0e5c-3902-87c4-f006d9dfca50 | -2.8393 | -54.12935 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2b43551-b98d-3e72-a550-32b9dceb8828 | -3.54222 | -54.65774 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b2d31b7-7085-32bd-91f8-6965e0111b60 | -3.83409 | -50.98925 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 962164f5-deb0-375f-8b0c-6ae5c2c23bb5 | -2.84212 | -54.07207 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3951523-6a3c-353b-80e1-020b9012b1b1 | -6.13863 | -47.9378 | 2026-10-08 04:46:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 593fff2f-3ba2-3cdb-aed8-a371d7ae85c8 | -5.88247 | -53.62833 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README102.md)
