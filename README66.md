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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a1be1f8-0bd3-37fd-afa0-2bf111133e23 | -14.32082 | -53.78623 | 2025-10-17 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 87b785b1-fd4e-35c8-885d-96f3d2fec1f8 | -13.39117 | -47.2123 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2ac3fa9-4dda-3dc4-9c42-f93623be95ed | -14.87081 | -52.42865 | 2025-10-17 04:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c9ba6a7e-ed3d-3b2a-a395-27c8d57647a7 | -12.96861 | -47.08689 | 2025-10-17 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e864ba3-a93d-3ac1-9ad5-431770958690 | -12.95762 | -47.93814 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97fb0f23-59d9-3d96-afaf-d5b1a688ca49 | -13.73136 | -44.33062 | 2025-10-17 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dee10605-3369-3879-b190-686aa8b058c0 | -12.28057 | -47.10918 | 2025-10-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8266f265-8fcc-3f1c-8ea0-076b1e1f41cb | -14.23767 | -54.91316 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bee3f2a-2920-391e-8791-8786c0103fda | -14.32154 | -51.44361 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9a9c42a0-6a30-3ba2-b49e-2a7934cd74d4 | -14.33341 | -51.44582 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| fc66f2ea-52b5-3367-bcf6-b1ffe7fc88d7 | -13.5074 | -47.16634 | 2025-10-17 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e835d744-1fcc-3d30-8838-54baeca9b4f6 | -11.6132 | -49.08519 | 2025-10-17 04:21:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eac37546-cb65-37fb-b9a0-d16dcf14e762 | -14.32789 | -51.44671 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| bfdb14bf-7b34-3d3b-9716-56fe3e31c035 | -15.82056 | -53.60124 | 2025-10-17 04:21:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8715e2e9-64b5-3c7c-926a-6023c878fc29 | -11.11856 | -49.23083 | 2025-10-17 04:21:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56700d73-f542-3a47-bb62-5ef24821f13c | -14.33129 | -51.43456 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c886e7d8-6311-3235-817d-e04f46b5d634 | -14.24054 | -54.90042 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4d0ffda-4f00-3bf8-9c5c-ae6fb3cab730 | -11.75454 | -51.14805 | 2025-10-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba54d6aa-967c-3381-abf9-17b503c686d8 | -13.4184 | -48.57781 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b044d810-8261-35db-bbeb-0bdbb309e892 | -11.97147 | -46.55073 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56cf8181-c953-3579-9d6b-119a7aa09cba | -13.25363 | -47.13465 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 43138fee-17fc-3f50-a296-e21185904f9c | -13.23658 | -47.11341 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f53728d7-0c84-3d8e-8354-35b000eb27bb | -12.42363 | -51.30036 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 718f457a-a1fc-318d-91b8-07376f41ea6b | -15.91822 | -43.52492 | 2025-10-17 04:21:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c32014b-52b3-3c8f-9dea-5f217f118c6e | -17.41553 | -42.43945 | 2025-10-17 04:21:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7942e53f-66db-3743-8a5c-a478672fd0b9 | -11.97091 | -46.55425 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b862e381-d2b3-394a-8eb3-14d89ed49b01 | -13.43512 | -47.96833 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71dfcb9a-699d-3b1d-84ae-6f5a2e3e274b | -15.58884 | -49.06667 | 2025-10-17 04:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 218481e4-bbb0-3503-8750-c59027d14775 | -14.32407 | -51.47584 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 652118ab-33ad-36f3-8995-5d0aa5c2ff72 | -13.41306 | -46.69068 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 729dd08a-21b2-32ec-b64b-c00237894b70 | -14.34041 | -51.45255 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 9e2268ce-6703-354f-9bd2-2b45af6a1ec1 | -11.77054 | -51.17787 | 2025-10-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cd4ca45-850b-3a0f-8806-c92472841fbf | -12.77414 | -44.8884 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 389d8db5-1fe0-3c9e-8f38-51a07b4f1d67 | -14.33221 | -51.4293 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c0c806f-c724-3cf0-a799-283bf7d89f15 | -11.51373 | -48.22848 | 2025-10-17 04:21:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67c3b753-5c29-38fe-af79-43948223796e | -13.25638 | -47.13878 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33d64ade-c918-3d5c-a196-14b4e404cad0 | -14.35229 | -51.47022 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8dbc809f-721b-3200-885a-dea49e519617 | -11.71181 | -44.26876 | 2025-10-17 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 345f138a-5f30-39cf-bde9-09c721d9cdb3 | -14.8938 | -52.4208 | 2025-10-17 04:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0edcf6d7-0a19-3389-bf48-3798be947cb9 | -10.95252 | -49.7633 | 2025-10-17 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 58d95132-30e4-3c84-b287-96a885ba6417 | -13.07155 | -46.93218 | 2025-10-17 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58f4a8a7-4f1a-3590-9105-8de06b109f7c | -13.71392 | -40.98652 | 2025-10-17 04:21:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1d49d0cd-f01f-3005-b7d1-03575e933735 | -15.82712 | -45.77079 | 2025-10-17 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88080a20-5474-3824-9907-698f8928c73b | -13.51072 | -47.16688 | 2025-10-17 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cce1a4d0-8ac2-330e-b692-1e1bb42bfbee | -12.7708 | -44.88787 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df5f0a34-fd6c-3e06-8b59-1ec8b751e854 | -14.09256 | -43.62662 | 2025-10-17 04:21:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67847eb1-6c21-35da-94ca-1c0c69f5fbde | -12.9708 | -47.0945 | 2025-10-17 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b62ae63-e6c1-37fc-ae8b-4f08b3897fc8 | -11.57396 | -48.5634 | 2025-10-17 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| efb50584-2f57-3e94-a495-4c55f4f87731 | -12.77469 | -44.88478 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 5608b00c-4bd0-3d09-9953-1a0bec38ce4e | -13.78186 | -43.6244 | 2025-10-17 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a17a80fd-3e83-3712-a32a-44b8035f1efe | -14.23445 | -54.90518 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12a57a07-0b10-3bb2-a448-3bd45c558f4b | -10.97934 | -47.89059 | 2025-10-17 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5389665a-b8a3-3507-b7ef-0f60f4e3b745 | -13.43236 | -47.96397 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ae5db56-e526-3581-82bc-f7dfb525f964 | -12.42233 | -51.30766 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c14ccbe4-5ae6-32ab-9eb3-4d50de26699b | -11.59031 | -44.06874 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b086613e-efea-3d48-8e4a-a2503bba43ed | -12.7758 | -44.87756 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34e4c949-2167-3dc2-9d13-6ae4bceeba19 | -11.58181 | -44.05602 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 723cc5ff-2965-3c83-a7ed-85a10a04d2a9 | -13.82674 | -42.35001 | 2025-10-17 04:21:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 589fe7b2-9dda-3935-b8a0-1e65fa66f8b2 | -12.16066 | -47.93343 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5de1c85e-3d1a-3236-912c-6ac55b4cd0bd | -12.43317 | -51.31713 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7b4e3ccd-5cf4-3c29-b2d5-30130da54b3a | -13.38863 | -42.7128 | 2025-10-17 04:21:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a335590e-5806-36d6-af8d-6529837d7a5e | -14.34072 | -51.44366 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 9d3b28fa-3a87-3e5d-a9be-7574f457d280 | -16.81112 | -53.91826 | 2025-10-17 04:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8411b7ee-bd17-3c16-a6ee-74548a880c24 | -10.85525 | -51.28887 | 2025-10-17 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dd8b8064-38b4-3c10-8755-806e3f6f2f03 | -13.75458 | -48.2265 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b049057-b040-3f0e-9e4d-aa5a6d32f83e | -13.23991 | -47.11396 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a78c2122-c1f0-3ef1-9bec-d476d0845629 | -15.78492 | -43.64697 | 2025-10-17 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fa22a2d-d018-3a65-bb93-a1544dd8b49e | -13.42679 | -48.08261 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ada548a1-7c4d-391c-9951-621c4dae94ba | -14.33882 | -51.45416 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| da46e268-d2d5-3f0f-80e4-79274092d307 | -12.922 | -41.82795 | 2025-10-17 04:21:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f6e862f8-6b69-325f-8253-8bb150d8ff77 | -14.32866 | -51.47305 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f7fa452f-dd71-3ed8-9d5a-ef5d6210291f | -12.58984 | -43.36782 | 2025-10-17 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a0d29bd-0cb2-30e3-92fa-e37c405d22b1 | -12.06439 | -47.98413 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b497579e-9e7d-3ace-98d2-8538222d08e0 | -11.06588 | -47.59505 | 2025-10-17 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc63d2df-56df-3d5b-ba60-ab562e032f4d | -12.72794 | -48.63372 | 2025-10-17 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62c6cc9b-a370-337e-802b-a5e842fa969f | -11.57328 | -48.56742 | 2025-10-17 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8f60ac54-2a82-357b-9c10-7802b7fc022e | -14.71947 | -48.3043 | 2025-10-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 160d81ea-861f-3d70-856e-7f869873baca | -12.42637 | -51.30838 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e0a37126-3fd3-3f73-8761-283465204fc5 | -12.78638 | -44.87552 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85ddfdfb-1f28-3a46-97f5-c6f5800ecd23 | -15.17281 | -43.53298 | 2025-10-17 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3a7344c8-bae3-366c-b379-9b7b3577bddb | -14.3057 | -51.44067 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02d881d8-2fc2-3e27-bbde-64d1a885a4ec | -11.7704 | -51.17725 | 2025-10-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6ed6de6-a23a-349f-b9b7-34356ba3a07b | -11.64668 | -48.408 | 2025-10-17 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8851012-6d43-31b8-ae38-fe6d4cd72476 | -12.91096 | -41.85058 | 2025-10-17 04:21:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1cefee08-af7d-33cf-a670-5375513a41e9 | -14.3358 | -51.47081 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 581a1a55-4a75-393b-913a-cee984f49087 | -11.477 | -45.07917 | 2025-10-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2fe1df5-d5df-32a0-bff3-b50a938036a0 | -11.52017 | -49.14508 | 2025-10-17 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1ecd5f0-03d8-3d7a-a9fc-7024ae812805 | -12.17038 | -45.05791 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38ba8809-c526-37a0-848f-f72a97eb8733 | -13.04735 | -43.03033 | 2025-10-17 04:21:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 96aedbee-efcb-3fb4-b72b-e5555e74f22c | -10.98243 | -47.91494 | 2025-10-17 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 660895f8-53fc-330d-b3da-2912ce214a20 | -12.78028 | -44.89305 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9852f802-d3bb-3d56-85eb-096f23204b8f | -16.54726 | -41.65128 | 2025-10-17 04:21:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d1a839a9-ceea-3bcb-8dec-960792f02de5 | -16.68664 | -52.13262 | 2025-10-17 04:21:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4f96f93-7c9e-365d-ad1a-b6612f559a8d | -12.27999 | -47.11277 | 2025-10-17 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6109312-5f06-3ba6-823b-c989780212b1 | -15.05505 | -46.61431 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf0e9be5-e3c4-31d0-baf6-9036dd127494 | -13.3981 | -46.72087 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d5af518-3460-3bcf-be4d-fa9945a7a7e1 | -10.94138 | -49.48103 | 2025-10-17 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 653fa5ae-5cf1-37fc-89ea-3fe30cad000a | -12.77749 | -44.88892 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| bba7054b-f6ab-3586-8d7c-2266a98705d5 | -13.48286 | -43.28963 | 2025-10-17 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ef75c96-a28a-32ca-bc3b-1b0d6d8ffdb9 | -15.01874 | -47.31647 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README67.md)
