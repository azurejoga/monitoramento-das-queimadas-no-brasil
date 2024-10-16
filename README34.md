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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c73d8960-8737-3798-9934-3a4003271e99 | -4.3858 | -47.48822 | 2024-10-16 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdc253f0-95c4-3d9c-a71d-5cb9702c7119 | -4.34486 | -46.69337 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eadcb62-78f9-324d-8ff0-c5b835eebe8a | -4.34424 | -46.69719 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c75cb9ec-5534-34bd-8b43-2398ae1577b8 | -4.3434 | -46.69609 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8cc1da0-86d6-3cca-aad8-bbe9d60e0a84 | -4.33937 | -46.70034 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f7025fc9-b3a0-3997-b8a4-f06a0738b1d9 | -4.33513 | -46.69954 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 261749e7-d8c2-3146-80e9-a20a5b0fb05a | -4.33006 | -46.73082 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78e25975-1b76-301d-9803-c6ec07bd3cf8 | -5.79229 | -47.33001 | 2024-10-16 04:06:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 804d0700-820e-3ff1-8636-edd49a2f5dfb | -5.7087 | -46.61996 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6addd88a-7ab2-37e5-967e-9d2417e3bd3a | -5.51451 | -46.90066 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5136079-3769-3698-bb1e-43eba0802f0a | -5.51385 | -46.90453 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a3fddf9-e428-3a53-a694-60c36594008e | -5.51319 | -46.90843 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 340fe9c4-c167-37d3-aca9-c79f53ea64bc | -7.64456 | -47.16309 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66b7f511-e46d-38d2-9abe-4a81f5ddcd50 | -7.64391 | -47.16686 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e143d1c6-2165-392c-88fe-f787bae93456 | -7.64041 | -47.16234 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b98edee5-3b8e-3e69-ac5f-3573d38dd442 | -7.63976 | -47.1661 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c90f64e-bf77-32fe-bcf1-4c165578732c | -7.6376 | -47.22852 | 2024-10-16 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c4e95ce-82f3-3eb2-b3a8-05b983750afe | -7.63144 | -47.16464 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5a7ef91-d0d4-366d-8e65-bdc6ef20e21e | -7.62729 | -47.16392 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c7b51b3-7010-3745-a905-02bd799e8617 | -7.51536 | -47.00203 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8cd23850-f61f-3852-ad50-c615c698abb0 | -7.18538 | -48.21152 | 2024-10-16 04:06:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72282858-f26d-3952-b416-c177c0cf4df2 | -6.95927 | -46.97058 | 2024-10-16 04:06:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a73d24d6-1e89-3673-b9c1-1a068aaee653 | -6.95864 | -46.97435 | 2024-10-16 04:06:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8683b39c-2b12-3283-a8a3-7cbaf1adf51c | -6.94652 | -46.99553 | 2024-10-16 04:06:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3d47f06-57b1-3858-8be2-226a24dd8358 | -3.22084 | -48.91936 | 2024-10-16 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2b25596-fba6-3a18-bef2-9fe23a1c47c3 | -3.22034 | -48.92228 | 2024-10-16 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f04ca235-582f-3c7e-be22-55bcfd26c6ed | -3.21984 | -48.9252 | 2024-10-16 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f60f952-c606-3468-85ad-790c984484ad | -3.21741 | -48.91841 | 2024-10-16 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a459df7e-f9f0-3611-a7a1-a65f4c8e9643 | -3.21694 | -48.92134 | 2024-10-16 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| bdea5ca2-2b54-3bb8-b8b4-c522d9459a27 | -3.21646 | -48.92427 | 2024-10-16 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8dbd548f-1539-3782-b350-853cddf5883d | -2.50449 | -48.55339 | 2024-10-16 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fed3e45-3f55-35b1-8fe2-b6163a3b5ead | -2.46233 | -48.34702 | 2024-10-16 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0078bfdf-a504-3517-89e5-4a5fec7ad5a2 | -2.46141 | -48.3525 | 2024-10-16 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7c17f6b0-a346-3d3c-85d5-53ad0f1bc577 | -2.46029 | -48.35155 | 2024-10-16 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fcb04cc4-fede-3ec4-aab6-04a329175daf | -2.16203 | -48.8114 | 2024-10-16 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd3ad418-3c29-3871-b1c4-621a7b5315f0 | -2.16155 | -48.81435 | 2024-10-16 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35dc6a56-900d-3201-a4c6-d0935cbcc717 | -2.45921 | -47.83953 | 2024-10-16 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a13255b4-fd04-38b5-b98e-ca48465759e7 | -2.38347 | -47.58671 | 2024-10-16 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 415ae52e-0590-3c19-983e-091a6770510f | -2.38268 | -47.59152 | 2024-10-16 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 676a4250-5dcf-3810-9252-14900837ae2c | -2.381 | -47.58973 | 2024-10-16 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d2a05d5-e8c5-3107-80d4-068f9196a5e5 | -2.3563 | -47.98862 | 2024-10-16 04:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a855ba5c-178b-37ed-a242-e375553ed1cd | -2.96466 | -48.00472 | 2024-10-16 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| b4f18f7b-a1ec-3a65-82fd-6dd2c9a002ef | -2.96029 | -48.00269 | 2024-10-16 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7fdbe573-7f61-33b8-8577-ca40158375ee | -2.95991 | -48.00393 | 2024-10-16 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 35d7f9dd-2064-35d3-8264-b0c2ab9399f4 | -2.95949 | -48.00773 | 2024-10-16 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 706d0558-7350-3bda-853a-41fb2f6ff5dc | -2.93785 | -47.98983 | 2024-10-16 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06566052-2812-3a2d-8ae7-766f1e672dd8 | -2.93735 | -47.99356 | 2024-10-16 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 451e7a73-e678-32e2-8816-70f014500407 | -4.81711 | -49.14068 | 2024-10-16 04:06:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e516f560-c182-358b-bd05-9cb306da7fa4 | -4.81675 | -49.14322 | 2024-10-16 04:06:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 127f42e4-b4b5-38f4-90ca-cedf12bb404b | -4.81607 | -49.38918 | 2024-10-16 04:06:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63cb0d21-674f-3687-89d1-618fff18e940 | -4.81556 | -49.3922 | 2024-10-16 04:06:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc2e2416-e0fc-32e4-9e73-be139e5ec112 | -4.36303 | -48.21686 | 2024-10-16 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69602e47-1a5e-3903-a123-2812da269713 | -4.36183 | -48.48955 | 2024-10-16 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2281dfb8-92a8-3835-950a-6e7983d435b1 | -4.3604 | -48.49051 | 2024-10-16 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1e38f825-9d0a-3914-8d7e-6ff0865f7db5 | -4.35952 | -48.49562 | 2024-10-16 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| befa2cbf-7b74-391b-9a6e-7ea433f3f263 | -4.35702 | -48.48875 | 2024-10-16 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b1bd18c1-b9bd-3504-bf48-ae2d3390e708 | -4.35618 | -48.49381 | 2024-10-16 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13e854f4-6381-3f07-8bcd-283879b28179 | -4.32963 | -48.6246 | 2024-10-16 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92d37e2e-4baa-340c-9fea-822886530451 | -4.32387 | -48.6292 | 2024-10-16 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ba78d51-791f-329c-9d92-6bafc87a1200 | -4.57419 | -48.01483 | 2024-10-16 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8ee74cb-e243-3f5f-a5ab-454b8c751e33 | -4.56874 | -48.01889 | 2024-10-16 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2437144e-4295-34a6-8d9e-5be4009cf04c | -4.56547 | -48.01991 | 2024-10-16 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f16846b2-a6f8-3979-8ec0-900bafc4f1fa | -5.2265 | -47.95662 | 2024-10-16 04:06:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ee99ab5-93d8-340e-8009-3698432d897f | -5.22608 | -47.9591 | 2024-10-16 04:06:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c335a59e-e581-368e-87de-34fc3215acf0 | -5.2257 | -47.9613 | 2024-10-16 04:06:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22969554-ed1c-3f87-a5c5-b5d2cd40d40e | -5.22531 | -47.96379 | 2024-10-16 04:06:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20abf15e-cf26-3632-ab5a-252aa8e8a577 | -5.22229 | -47.95355 | 2024-10-16 04:06:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4beebf06-bfdb-30fe-95ac-612d773da8a8 | -5.22195 | -47.95578 | 2024-10-16 04:06:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d05a0de9-b455-3f91-ac54-9c9f1d6ff56b | -5.22153 | -47.95823 | 2024-10-16 04:06:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad860b4c-1aa7-3ff0-bb3f-30691b2780e7 | -5.22115 | -47.96043 | 2024-10-16 04:06:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb02a69e-bf38-3709-89f1-2c2198ee8afe | -6.66209 | -49.46368 | 2024-10-16 04:06:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf1f4bc1-3366-3776-8ba8-6779e719f57e | -3.44701 | -49.73796 | 2024-10-16 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16f8202b-55e6-34b6-9e21-eb2d06710146 | -3.44644 | -49.74132 | 2024-10-16 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd9f7dcd-3ede-3dbb-9403-939eb66593e8 | -3.4417 | -49.73706 | 2024-10-16 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67c59b42-4601-3c23-930f-7aafac4257b6 | -3.44114 | -49.74041 | 2024-10-16 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4553d73f-1abe-31c0-90ed-6dbc60284212 | -2.83787 | -49.53325 | 2024-10-16 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 478047bd-5291-3dcb-bc0a-e76f37028a3f | -2.83733 | -49.53653 | 2024-10-16 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59599bac-69fb-3da8-bd51-ce8add6caaeb | -2.82455 | -49.54782 | 2024-10-16 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b3e9f1d-9d9c-322c-b6e8-dc226ebbfb05 | -2.82401 | -49.55108 | 2024-10-16 04:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3db76348-08be-3fe2-9d9b-b16e0606158c | -2.6287 | -49.27612 | 2024-10-16 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40de5b54-cede-312e-825b-5b21119122ce | -2.62293 | -49.27855 | 2024-10-16 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c2cb418-8772-3f15-8531-ec12ce30f097 | -2.61483 | -49.09761 | 2024-10-16 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3582702-1dc4-342b-aa32-cebdbcdef788 | -2.61432 | -49.1007 | 2024-10-16 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 731ea4d4-d5ce-3baa-bb89-d41ceb90c264 | -2.60198 | -49.11132 | 2024-10-16 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09a9c469-9e87-345c-b1cd-d870dd82d362 | -2.60148 | -49.11435 | 2024-10-16 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1c7b84e0-ec3a-3de1-bd5e-2433ce1f0388 | -2.49623 | -49.07154 | 2024-10-16 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07c209ac-f00c-3243-9af5-bd5795ebba03 | -2.49573 | -49.07458 | 2024-10-16 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4f92629-88b7-3fcd-b448-97544ffed44b | -2.43893 | -50.23804 | 2024-10-16 04:06:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb0e652d-e686-3e76-bf96-177db09e8e16 | -2.43395 | -50.23345 | 2024-10-16 04:06:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2878b592-48f3-3d4e-98d8-667d148f7e65 | -2.43334 | -50.23716 | 2024-10-16 04:06:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ab6d5da-5395-3d78-9c06-ff674c63598c | -2.43128 | -50.18014 | 2024-10-16 04:06:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 783ec5f7-5a04-3a34-a45e-1188c1a8c1d4 | -2.42572 | -50.17918 | 2024-10-16 04:06:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a089c32-73c2-3372-8f25-fd12414f5872 | -2.39933 | -50.30384 | 2024-10-16 04:06:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb82f92b-167e-33fd-9cab-a9892c0dfe6b | -3.6985 | -50.11774 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16065231-e7f0-36ce-8306-49be871ee821 | -3.6925 | -50.12019 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea103ae2-8b9e-31de-93e7-4c30117f7e88 | -3.58583 | -50.57541 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 58dd8399-3789-3d64-8ef0-9eb0ddd05bce | -3.58519 | -50.57907 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8473b274-dd83-33d0-91bf-57513b798aeb | -3.58301 | -50.57436 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aad65545-a6b3-3292-90cf-4f8bbe0c60a5 | -3.5824 | -50.57804 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a00df255-5699-3f99-bc00-8ada9e2bc1f4 | -3.58023 | -50.57444 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README35.md)
