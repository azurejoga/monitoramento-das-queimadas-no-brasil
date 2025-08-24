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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b31134b2-d4a0-33d6-9034-0c8fec787fec | -11.10729 | -44.76908 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20a7bf13-16e8-3c1e-8fd4-a07875ab9732 | -6.9564 | -44.42414 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c043bb4-7131-37b3-8441-13556301f1f1 | -5.58238 | -45.81066 | 2025-08-24 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a88e0888-9520-348b-82b0-d5acd756a450 | -7.0205 | -44.65016 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 739f68a0-07db-3bc1-93ee-4549df9ce08a | -10.57156 | -47.13443 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78789203-d85e-32a7-90ff-9cec7dc034d3 | -10.40901 | -47.17795 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87558816-773b-34d6-bc00-30477e73fe99 | -6.88473 | -45.67218 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d5b1d14-f449-39ae-b88c-c6ac53858ee9 | -10.40473 | -47.16815 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52bc55fc-c32f-3b8a-aa0b-73f549a4c360 | -6.03904 | -44.00057 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cbebcda-5909-3911-9ccf-b27fda5716ea | -10.40274 | -47.19467 | 2025-08-24 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14e5b3fc-b3af-34db-9192-a846f5100dd5 | -10.54905 | -47.13764 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 628203b7-ce6c-3db0-96f4-57ed3e8ce0f0 | -5.48808 | -41.40945 | 2025-08-24 03:42:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 213769a6-f95c-3249-b61f-7283978f5e92 | -6.87741 | -45.67999 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e704d2df-81aa-3d43-9563-9961b112d77d | -9.79652 | -46.42926 | 2025-08-24 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2272c211-2336-3b2b-9871-9c8609db1c3a | -7.6078 | -45.24646 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d83ae1d1-a7a0-3490-ae35-4211082aa771 | -6.09037 | -44.69024 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebdb7a35-265b-3f01-bdaf-89a828a8adc1 | -5.88013 | -43.39048 | 2025-08-24 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0d79cc6-8a6a-38f6-97f8-5b319514f0f3 | -10.4078 | -47.20027 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94fefe73-fb3b-36b9-a924-d01a9b7e72bc | -6.18648 | -45.43098 | 2025-08-24 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| baa3813c-34f5-3712-ab88-b09dbcae755c | -9.11211 | -45.19084 | 2025-08-24 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9ef879e-d5b3-3785-96ef-299063f81418 | -8.75494 | -46.75205 | 2025-08-24 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60cc0400-1157-32b5-8681-7d3ba9c24257 | -8.05497 | -45.00627 | 2025-08-24 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e969948f-0857-3e48-86eb-5b63a719a246 | -6.20185 | -42.98153 | 2025-08-24 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9cf6245e-74f6-3613-a7fc-f63b56be5f85 | -6.23108 | -44.1339 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 74176d01-e10f-34db-9a87-03d16a4e0669 | -11.11002 | -44.78211 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afc994d3-8d3d-3b74-89c7-fa3b09ff28d9 | -8.01713 | -45.49358 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 58c00eec-c698-33c2-a78c-87c0bb404cb9 | -10.57483 | -47.14907 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64ffecd4-b168-3dcb-b153-ee70148aad5c | -7.70342 | -42.12973 | 2025-08-24 03:42:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 24a71e55-4d89-3d78-ba35-3b06e40871e4 | -8.77389 | -49.96828 | 2025-08-24 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f92315b0-3a52-36d9-8b3e-6337c89ce09c | -6.03756 | -44.00516 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 077c59a4-fb68-3195-9cb6-5f3fed33b315 | -9.24694 | -48.19783 | 2025-08-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 73667986-4d99-3175-92ba-279e203224f5 | -11.11391 | -44.78907 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08428b5f-9db5-3d68-9d0b-3dfd1df19cbc | -6.18579 | -45.43489 | 2025-08-24 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61dd6c8e-a3d0-301f-9bcb-d4e8b5aa391e | -6.03856 | -43.9993 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a701eb42-e4d8-380d-ae60-887d1912c45f | -6.12572 | -44.39483 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b6e509c-d9fd-33d5-ba19-0566b2276680 | -6.10067 | -44.69556 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7043f234-6492-3cb5-bdda-1910f5546bf2 | -6.31258 | -43.76744 | 2025-08-24 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce15b5f0-2ffd-3743-b949-4cf5c7f8c8af | -7.29797 | -43.66911 | 2025-08-24 03:42:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fb3d5e08-ff21-39db-a093-fc5ff42a8b89 | -6.18717 | -45.42706 | 2025-08-24 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 76e2ae27-ff28-3d2f-9d72-eb7aada41b86 | -8.76594 | -49.9831 | 2025-08-24 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3643b44-efbb-33d2-a5d9-8d72c6f61e0f | -10.8124 | -46.3918 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6068833-3114-39a8-b731-8d2a09631eeb | -5.97999 | -44.27739 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a047a35-512b-3cd0-b6ac-24649e83f522 | -5.41501 | -44.99059 | 2025-08-24 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9fe2414-d573-3933-9337-62434f3a61a5 | -11.15494 | -44.70875 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebaf4860-e61f-32b1-94aa-88dbbee76ecd | -11.10786 | -44.76605 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 280589ce-6af5-37ee-a6c4-dd4778808cd2 | -5.88161 | -43.38191 | 2025-08-24 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54aaad66-b0ef-3b04-bcdd-a2b72929147e | -8.21741 | -45.11531 | 2025-08-24 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb4667fd-5bed-3e55-97ae-3ccca3b48bb7 | -5.65704 | -45.153 | 2025-08-24 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c31eb58e-9889-378d-8d86-c3a4fb67b133 | -9.67896 | -48.35476 | 2025-08-24 03:42:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab0671d6-81d7-3b15-a246-2c5b57e3aa32 | -6.6124 | -48.04993 | 2025-08-24 03:42:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f79428f-2aa5-35b9-8a00-d5a215e3b416 | -7.01629 | -44.64264 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 001a1965-39d6-3ded-b47f-eb2dfecfc8ef | -6.58792 | -44.5639 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e912e9ff-6d92-390a-88f5-e7642962ded7 | -10.29793 | -46.75526 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 133880f7-7fed-3955-a98c-b725e7d0b258 | -11.14232 | -44.74853 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a6b4568-8039-3b0e-86f9-3b403e91398d | -8.76094 | -46.75289 | 2025-08-24 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7517c7b6-b789-332d-bf18-3c1f7df30902 | -8.76239 | -49.98877 | 2025-08-24 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c7f231e-355c-346e-90de-03479f13e34c | -7.18331 | -39.29339 | 2025-08-24 03:42:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 310bc7eb-3d7c-32f0-a3b6-16b81e132acc | -7.58983 | -45.25148 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8a74a4f-d7a7-3904-9794-f432f030ff85 | -7.17777 | -44.66851 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 578543ea-3d08-323b-ad73-49acf569ddf1 | -9.14254 | -40.31686 | 2025-08-24 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c3d0365d-bd46-3ca7-afa6-05de1d737d40 | -6.60566 | -48.04916 | 2025-08-24 03:42:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc22a701-8e23-3359-8b4e-7585ec1f335b | -9.79778 | -46.42808 | 2025-08-24 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f300f0d-76c3-3360-a99d-96a4fb314f52 | -10.4072 | -47.17225 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be9d7f0d-c3a7-32bf-af5e-95a8f73eed30 | -10.40388 | -47.1726 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29458755-326a-38e0-8e3c-9b37b6222b8f | -7.01689 | -44.6392 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fc94a3a1-195c-3739-bf74-faf4b06c54f4 | -6.08979 | -43.80539 | 2025-08-24 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc396fe0-1549-3bee-bbf6-742eeada9f66 | -6.89117 | -45.66928 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14abc76d-ff01-38a7-9fd1-adae9f8e4d13 | -6.12686 | -44.3884 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8a66605-4274-36a3-b1c1-a39d42d741a7 | -6.88749 | -45.68975 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6c82f7c8-4361-3efc-9d1b-08dbf9418a03 | -6.3085 | -43.76085 | 2025-08-24 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e706f837-d6aa-34e9-bf95-5b88f764b9e0 | -9.02621 | -47.65001 | 2025-08-24 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f8be57d-274c-382b-a330-c890aa753a84 | -5.4094 | -44.98955 | 2025-08-24 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 58bc52c7-c405-3aff-8424-b81eeb977ab2 | -7.48271 | -44.9297 | 2025-08-24 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da72feb4-6f8c-3789-a554-dce1a4327c7d | -7.02167 | -44.6434 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d06ca80d-f590-3117-837e-e76ea970372e | -6.7964 | -44.99484 | 2025-08-24 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f709216b-ce6b-3d15-a3dd-bbbe9d60ff2b | -5.4932 | -41.4059 | 2025-08-24 03:42:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 40ff9974-4876-372d-9a32-d267a065c1d5 | -8.75411 | -46.75655 | 2025-08-24 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c379a21-0788-367f-a7e5-b4c0944a8ccb | -6.89544 | -45.67841 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba4f49e4-6904-3130-a1c0-b61a77ebac42 | -7.02048 | -44.63711 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 65f1d0cf-295f-321e-8615-79c836f9f5ed | -8.76384 | -49.98139 | 2025-08-24 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31ec825f-8c8d-3aef-b115-47fe2fce18d3 | -11.14287 | -44.74562 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1780df0a-28c5-3d2d-b6c0-8a7bc7a81910 | -6.09458 | -44.69821 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faa41244-c7c5-3ea5-9333-0d7b529fdacc | -11.14074 | -44.78472 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46d560b1-daa2-3411-8a9a-1c84a9ef40ad | -10.29788 | -46.75486 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14db1415-afe2-3200-aa0e-6df56b1bf103 | -7.61334 | -45.24728 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dda9569f-d5b8-32cf-94a9-2fc26baf3a5a | -6.77341 | -43.28285 | 2025-08-24 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8bf01db8-bd17-3102-871e-e24f5bcf421c | -10.29207 | -46.75384 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a1b3112-259e-32ce-afe4-18efeb6e49c1 | -10.82549 | -46.41439 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1f681738-cbee-3c3f-ae6a-92a27493dc2b | -6.03905 | -43.99644 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b070c736-27cb-3f00-bc0a-419a57131406 | -7.92177 | -45.9216 | 2025-08-24 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1d30459-8e3b-3304-9394-680f2e330734 | -7.02519 | -44.64154 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b983a7b-fad3-3144-806d-1a8c32508c42 | -6.59061 | -44.56554 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b22dc07-9697-3357-82ac-1bc15239ddf6 | -10.81651 | -46.40063 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bea5569-441f-3b6e-89d4-82291452caf9 | -11.10615 | -44.77509 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2eee6898-576e-31a0-a67a-a56734dd1990 | -5.88514 | -43.39133 | 2025-08-24 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 030acb0e-39e4-3354-bcce-0d1aef3449c3 | -6.89251 | -45.69476 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3b5f4ba6-850e-3bc0-b3d2-49f240a425bd | -5.74783 | -40.44485 | 2025-08-24 03:42:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dfadc522-9619-351f-8ec6-b0d0d038f56f | -10.29213 | -46.75418 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8721a1dc-d926-30af-86d2-4d21f3f0faa8 | -9.11744 | -45.1919 | 2025-08-24 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7fa869d-db7d-3fc5-9fa6-5dfc3a59d7ea | -10.57573 | -47.14444 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README24.md)
