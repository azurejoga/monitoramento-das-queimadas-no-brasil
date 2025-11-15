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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec25f3c5-c1bc-3ba8-b291-af6e8a980da6 | -3.85586 | -44.00085 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b32ce6b5-9872-3e66-b597-0fdf45b17bfd | -6.03179 | -45.80825 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a8ab114-1780-3b88-b50e-27a78e281cf5 | -4.0173 | -48.80792 | 2025-11-15 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9b1b52d-9145-36ee-b24f-90229156eb19 | -4.33052 | -47.57121 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db8b2abb-b5cb-3795-9762-d90a63b06c1b | -4.04567 | -48.0979 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 466d0dff-acba-3ded-89f8-891912eef73f | -5.38012 | -45.37197 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76b46a71-88ee-3387-9d69-b044b5f996ac | -3.19853 | -51.37312 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cced5773-672b-320b-a316-942cf053daf5 | -5.47689 | -40.97068 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 23e542c7-3bc7-3873-8e3f-5901c6fca09c | -3.52288 | -56.3233 | 2025-11-15 04:25:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3529889e-3e70-32e7-a396-43c85c5824f8 | -9.45867 | -44.87402 | 2025-11-15 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf555ba5-d3e2-336c-8e9b-696f006a9047 | -4.67828 | -45.27682 | 2025-11-15 04:25:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fab197df-0485-35b0-ab6e-f0334ad30185 | -3.98481 | -47.99862 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b97ff86-5e7f-3864-b1a2-03015cf8c2d4 | -4.66951 | -45.05072 | 2025-11-15 04:25:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbb7390f-62a1-3343-a633-2208957adada | -5.28136 | -49.28221 | 2025-11-15 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ac198f3-0421-30ee-ac3b-9b482bcdb56f | -6.15584 | -48.04206 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d59f7bfe-a547-3743-9313-fcb9a61986cb | -4.50728 | -44.58918 | 2025-11-15 04:25:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb1080ad-ad00-3e27-afe8-08d597de206a | -4.54929 | -43.21911 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be30d919-8662-355f-b4d2-886c27c4d099 | -7.33525 | -40.3723 | 2025-11-15 04:25:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a13d9e29-e499-3338-af52-b6d806c17e8d | -7.38805 | -48.6469 | 2025-11-15 04:25:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6723c228-55ce-34af-8c40-936857d2f084 | -4.68298 | -45.85007 | 2025-11-15 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3db1e8b7-3a39-3941-8149-b66a4e94dd85 | -10.0508 | -45.35349 | 2025-11-15 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 016ebb1f-195a-3717-aa5d-5ca97fbefe8f | -8.5702 | -46.06162 | 2025-11-15 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00e061ee-cb57-3a68-bb6c-09ea1e2182a2 | -5.03872 | -43.60844 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2ef20cd7-ca6f-328a-9141-199ff2af386d | -8.58533 | -48.74788 | 2025-11-15 04:25:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9625b303-a7db-325b-a95d-716735d46162 | -4.05508 | -46.4255 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0b261144-0d0e-3815-85db-bbb481bb564c | -4.20891 | -48.56781 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b8396b3-417b-3163-8345-336c3f882916 | -3.20421 | -43.34887 | 2025-11-15 04:25:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c6dd357-b1d3-3ded-835b-e1de889d3014 | -3.36882 | -45.50173 | 2025-11-15 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d171d58-6537-3402-a1c4-16762bf29938 | -2.36238 | -46.51379 | 2025-11-15 04:25:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9a2b691-2b95-39da-a5fa-0edc0954fed6 | -6.97086 | -52.8726 | 2025-11-15 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b28fec3b-a2de-30dd-b774-65f0ebb245af | -4.42351 | -43.3526 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 758ac089-9fb2-30a5-ac49-6069235dd3c0 | -9.0148 | -44.17454 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2d50ebe5-6eb2-3961-a7e8-a8c4c8e57a98 | -7.21549 | -47.97824 | 2025-11-15 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78b12ece-9ef4-363c-802f-fd177b2fa1df | -5.43091 | -43.17784 | 2025-11-15 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f3fd56e-aa4d-33fe-9dc1-be8795bdadfc | -3.47785 | -50.03498 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ea91fa4-5b10-3e7d-9ea2-1a080c01b334 | -4.05231 | -46.42152 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85377920-ced9-3d09-82ee-5c59af78e80b | -5.46342 | -46.80188 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3e3a8f1-0f8a-34ce-8cf7-b3e971e508bb | -4.30381 | -45.88486 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff2b6276-e4a0-38fb-bbe0-34f54b03b856 | -9.52145 | -47.26966 | 2025-11-15 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22dc0241-ed5f-37b1-ad17-f92e3f89e950 | -3.65311 | -44.79588 | 2025-11-15 04:25:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0efe10fb-cba1-3d15-963e-f1f7e296589b | -4.01013 | -48.80676 | 2025-11-15 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2a5759e-1d1d-3503-be6b-47e3e844cd56 | -4.32314 | -47.57372 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5d19948-3c8b-3b6a-ab8f-779c534a92b1 | -2.88607 | -51.43148 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd33c992-c5a6-3870-8720-252623b536a5 | -4.59808 | -44.31731 | 2025-11-15 04:25:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c4c9f7d-d215-380d-9f73-e8da4425e028 | -5.82409 | -46.47903 | 2025-11-15 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39523c56-8fc2-39ca-ac40-050b5a9ce588 | -6.15184 | -48.04519 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4eebbb64-c21c-3749-9c0b-31a01457a625 | -4.7559 | -48.84005 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fb79728-37ce-3c36-9e41-5bf15aa361af | -4.35134 | -46.48662 | 2025-11-15 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0d201063-33d9-388b-9ebd-3b4059cd0c0f | -6.27381 | -41.75492 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 20c4c565-434f-3b5a-acae-2affa042dab7 | -4.62047 | -42.81006 | 2025-11-15 04:25:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 917e9082-1e68-37b2-8dcb-b4c519fada1d | -5.12203 | -55.97345 | 2025-11-15 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30428a82-d63a-36d5-9a3d-9883752ec54e | -7.45322 | -42.76508 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 80ca4db0-b321-3f3d-ab95-5bdf0fbd027b | -5.47347 | -41.40071 | 2025-11-15 04:25:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2036188e-3680-33f2-9978-1964efb0a76d | -8.99951 | -44.18026 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e2a2245-cdcd-3860-a758-41ca3d6de2cb | -3.99073 | -47.67613 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 51b7e6bd-80b3-30aa-9824-b4f89b43e143 | -5.16643 | -44.85075 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 322000df-67e7-36ef-b08d-4fc669919e17 | -5.47741 | -40.96717 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| faab69f0-d897-3847-97a6-56ebafddc0bf | -4.41094 | -50.81928 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b93c72b-46ac-315d-9c6d-2428cf163078 | -6.28548 | -41.75669 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b6a08073-a64e-35c2-876d-8e8d2668b8c4 | -4.85804 | -43.25943 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9997c6d1-5229-3284-a192-596acc944d8f | -5.42731 | -42.57601 | 2025-11-15 04:25:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47930609-b948-3c33-9f22-0c0107304da1 | -2.43019 | -48.0475 | 2025-11-15 04:25:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0fbc460-e2ca-34cc-b017-24aa0a2d9842 | -9.55054 | -47.76997 | 2025-11-15 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75daf130-dae8-3a2f-a365-4dd9d0db08d8 | -4.70348 | -40.1216 | 2025-11-15 04:25:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a8520639-4113-37e6-826f-fe34788af568 | -7.80981 | -48.59764 | 2025-11-15 04:25:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2055b3b8-2519-3ef3-868a-5056fd4edcd0 | -9.93931 | -44.93347 | 2025-11-15 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4880235-7e9e-3656-935d-06b55924e2c4 | -6.4096 | -41.46482 | 2025-11-15 04:25:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 35328880-f37a-3fe0-b70d-7859bfc2f3fc | -3.85989 | -41.87704 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7cc79b01-bec1-3225-9a62-3127b008b0ab | -8.30083 | -43.80122 | 2025-11-15 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e6acd8c3-f3ec-3bec-9502-40e5b939ca42 | -4.73353 | -47.15786 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 8513deaf-34db-3f19-8c0a-603ed2d93c30 | -9.13041 | -47.12113 | 2025-11-15 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29ca1382-08b3-3c4d-adca-51c9c38c1afe | -4.99233 | -47.51426 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa0cdf1b-d731-35e1-9be6-ea3380a60a18 | -7.53906 | -45.85643 | 2025-11-15 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86c667a4-ad28-30c9-a9f6-02b915d8f63a | -3.72831 | -50.61067 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d6fc93c-ba20-3eb7-9956-9e561a080d20 | -5.99826 | -45.39372 | 2025-11-15 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8c9afc0-cd67-3d29-92be-ab1a5c677537 | -9.48507 | -47.28524 | 2025-11-15 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a12fff94-46c8-36d0-9f32-263c2d94437b | -4.9805 | -43.89048 | 2025-11-15 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0befff7a-e931-3eef-8c2b-2b3bcc08343e | -7.10813 | -42.73515 | 2025-11-15 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 889cfcc6-78c2-339c-b091-50e84a21da81 | -4.25662 | -48.65189 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6bea0b3f-720c-344d-8918-4b2e5083a807 | -4.49864 | -42.87226 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3b08838-8d64-3e49-98cb-9af3b491a383 | -6.15525 | -48.0457 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 40cdcedd-aa0f-31a4-9102-e3234247453b | -4.91203 | -49.9981 | 2025-11-15 04:25:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76d91072-143a-3bc7-85eb-0a99ac8ad432 | -3.19401 | -53.01609 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bd27b76-8fa6-30e3-91b6-3291794eec27 | -9.00518 | -45.46317 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dc143ed-9bf3-3bc2-9946-01d85cbca56e | -4.81219 | -41.61715 | 2025-11-15 04:25:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b32d222-95f5-301b-a827-d7177e25a4af | -6.81604 | -48.82424 | 2025-11-15 04:25:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ebafc95-789a-3282-8c84-2589b4aeef81 | -7.72527 | -45.81793 | 2025-11-15 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6702457-ad0a-3549-9c05-62053bcb641b | -6.88025 | -41.58081 | 2025-11-15 04:25:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ccefc75a-1db2-3720-be29-fec79f3b16b4 | -6.00645 | -47.90548 | 2025-11-15 04:25:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0aaba0e7-7959-3967-b18b-dd4dcd6298d4 | -5.91798 | -46.52932 | 2025-11-15 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60505630-9cad-301d-96e9-7254acb8a7bb | -4.39724 | -44.07907 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b61a630-7be7-3401-891b-b286f039c95f | -4.39769 | -45.82952 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2239014-d792-3e50-9b60-4ebc542f272d | -3.99414 | -47.6767 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9918d8ae-7151-3218-af33-05db8e64b780 | -3.70665 | -47.63261 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c962ffc9-1a27-3427-b465-e297fc82e928 | -4.25304 | -48.20458 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| df714ed1-0f82-3c16-9489-c29bc819b9bf | -5.73496 | -51.04635 | 2025-11-15 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af19f3bd-f30c-3227-979c-9171ff6b6998 | -3.60046 | -54.67685 | 2025-11-15 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb825933-def3-3f2b-a091-02c6d54c70d6 | -5.41893 | -43.25886 | 2025-11-15 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3b856437-5b44-38b8-9910-7576786ee83e | -4.98826 | -44.17882 | 2025-11-15 04:25:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8111120-6a69-3731-acb6-8edf6c5fb6c7 | -3.24342 | -48.84204 | 2025-11-15 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README38.md)
