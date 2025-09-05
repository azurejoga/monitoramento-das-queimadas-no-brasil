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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a200069d-3252-32c0-86f1-1991b9c748d0 | -9.71499 | -51.08148 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60da3cd8-a243-3e30-835e-6fa2b16b43fe | -12.50186 | -48.07576 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9defec7-2e49-3d11-a20d-193ac48efa93 | -12.95436 | -48.05739 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3576461e-2168-32c1-9285-71afbd7c0094 | -8.9723 | -44.45242 | 2025-09-05 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f87ab313-0b44-3a75-acfa-8d4debd3e184 | -8.34731 | -52.51967 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5f103d70-b793-379d-858d-a8e645fcf519 | -10.72576 | -47.95206 | 2025-09-05 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04836c1a-b01e-32ef-963f-1837993da43f | -8.32754 | -47.52847 | 2025-09-05 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 590508f8-4ba6-3129-ac22-d1b55b6e6c9e | -11.59823 | -52.17697 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ee5034c-5e29-3622-a26f-599318f6798c | -7.59098 | -49.72404 | 2025-09-05 04:36:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 333360e7-bc2e-382a-b498-317e03ce5529 | -8.02424 | -45.41567 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9e1c8d4e-cc4d-36e8-90b9-0f3d174a98aa | -13.73996 | -44.70033 | 2025-09-05 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b6b6df1-e607-36ba-82a7-5284c4af9cc9 | -13.71474 | -46.91105 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32182f8f-cabe-3635-bc8c-4f6564631aaf | -11.39365 | -43.59909 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d0063ea-c3ed-33d1-a85b-3cf6b74451eb | -11.00356 | -47.15974 | 2025-09-05 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d841d2e5-d4af-38fc-abd2-a977423db067 | -11.84759 | -51.44331 | 2025-09-05 04:36:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a40de69f-6b20-3eca-8271-8de93ab61df7 | -12.87429 | -48.00816 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04c653c9-9544-330c-a35f-a2bb92ee0163 | -11.38437 | -43.60548 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2241bac5-ab7a-34be-b573-e81953ba1885 | -13.30109 | -46.81362 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b82a7ad-ac36-30f0-b11e-a664030a776a | -12.9583 | -48.05426 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c28d263-e2e7-30e5-a670-aff1577fcd56 | -13.27934 | -46.81462 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adfd4c5c-bd5f-39b3-9ae0-99973f55940d | -9.83214 | -47.81134 | 2025-09-05 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c1eae28-3e5f-38fc-8236-7ca57a74098e | -10.47922 | -53.62242 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17cb97db-8eab-356a-b960-22f2d18d99b5 | -13.35623 | -46.83065 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b48524d-fbde-382e-bb37-139728f4e6dc | -12.90268 | -48.07893 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7464ad36-0a4c-37f1-9d28-19621cc73c9c | -12.92231 | -48.06355 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78da97ca-7ef1-3858-b559-c1740f44be22 | -12.94761 | -48.05633 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a1ec0fe-5115-383b-8d03-8a7a7521b964 | -10.98975 | -49.769 | 2025-09-05 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 932e0ea2-2d3a-3b03-81b9-c12fe0541d67 | -11.72578 | -47.75033 | 2025-09-05 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f61d7fff-9335-3a13-b608-55d7a2fc7441 | -11.5982 | -52.15516 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c68c7310-82b8-3bba-a00a-23e42b48b746 | -5.50603 | -60.12459 | 2025-09-05 04:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a1a7860-9b49-38a3-96c0-3a2ff4aa39fd | -8.64993 | -54.85154 | 2025-09-05 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f9e24b9-99ba-3f1d-8e47-26111ae7c89a | -9.07163 | -50.43218 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c3bd31b-ff6f-32e6-9c43-d0751f81fe62 | -9.00189 | -45.51731 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0a824e6-677e-3fd4-a8b5-81350b7b7fdf | -7.98921 | -45.45543 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81c6fafb-7d64-3b7b-b149-f5d9d3c0d3a6 | -9.79881 | -48.30764 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a114eed-6a45-33b6-bcf5-425e801bbe27 | -11.8603 | -51.45343 | 2025-09-05 04:36:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 262a563f-b3c5-3387-8c0e-d565413438fb | -9.96966 | -51.65865 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a61c84a9-2fc1-33f2-8919-6a44a2e7dcdc | -11.63238 | -52.21797 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 478c0510-abfa-33e8-aa44-0f08a6ebc83c | -11.6473 | -54.53716 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 52946739-7a1d-37d4-bc20-0cf1dbe673be | -8.86921 | -52.02575 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cdb2b8c-b742-33d6-a305-4c329b394332 | -7.76193 | -48.7848 | 2025-09-05 04:36:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad632149-bcc6-3598-8334-6ecf96f2b611 | -12.89298 | -48.02936 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ce12c1c-0417-3e5b-8ddc-5f94697f7a51 | -10.51986 | -57.77833 | 2025-09-05 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a3783cf-e4be-393f-b377-b8e1ce83cb33 | -11.58591 | -52.18364 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c424cc5b-8b15-3d03-be42-db3063a0d991 | -12.96223 | -48.05114 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 190c9d06-be7f-3d76-91af-838e1582f395 | -12.89129 | -48.01777 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 642bdcbe-91cc-3399-92c4-a0e5b1ca85df | -13.00296 | -48.06088 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a85d795-b3a8-3b5e-8643-ec3d192b81b5 | -11.85875 | -51.44107 | 2025-09-05 04:36:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87556a50-3813-394c-adb7-04179800727f | -12.50412 | -53.83341 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 361ddf73-8dbb-3724-9788-f48d37bc2220 | -10.46324 | -53.61967 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7de6c22f-fd30-3439-9a25-624cf42208ac | -11.97114 | -46.77871 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5d8d123-845a-3f96-8289-aa211ed2154a | -13.46637 | -46.83867 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bed27ee2-bf1c-3830-b5f6-26b11de55244 | -7.72313 | -50.31019 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07da6b4e-93f5-358c-af5a-4cf9d2f0ec1d | -8.09532 | -45.34664 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8cae4325-60b6-3356-bc6c-958c7bf0e7bc | -11.67884 | -52.16323 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05e8606c-da4a-3bfc-94ed-1c51c4c1cc98 | -12.71403 | -45.09028 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 82eecbb1-ccba-3021-a5ae-4c283a3c9cb1 | -8.21138 | -49.59958 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2ad9240-b17e-3a36-bb7b-72680376b77d | -8.09649 | -45.348 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eb9795ad-1d76-3391-ae87-a700b62ef75d | -11.20197 | -55.01719 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 941085da-deb0-3359-b4f5-9a8a78244958 | -11.60257 | -52.17337 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca0ee0bc-8911-3986-b36f-5b41aab04f89 | -11.85744 | -51.44897 | 2025-09-05 04:36:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d22953b-e8b9-30b8-b344-a1c517748429 | -10.0988 | -48.07465 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97ff80fa-3f4e-3765-b761-103c5e81cb0b | -10.98213 | -46.00776 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d5e7c0e-7e7d-3a8e-9680-a66b0f07b34a | -9.42796 | -46.76961 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7397a186-325b-36fb-a8c2-82da0056fbe8 | -12.91716 | -48.02942 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7eb24533-e2c5-392d-8992-c75a6090c7fa | -12.09621 | -44.72597 | 2025-09-05 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee394124-55f5-377e-a6ee-d01f8dac3059 | -11.63018 | -52.20882 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 626fc058-2e73-39cc-9e1b-6d00d665a17e | -10.76912 | -48.2892 | 2025-09-05 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e865f75c-93a6-30b0-aad7-d2577d9cd929 | -10.85344 | -47.27618 | 2025-09-05 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24529bcc-92bc-3f0a-861c-d1e5c998cde6 | -11.67292 | -57.34752 | 2025-09-05 04:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 428ac76a-ba9f-3275-80d2-d5d4e920dced | -12.53412 | -49.10417 | 2025-09-05 04:36:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23340302-09cc-3f87-b114-378bcd22f081 | -8.02304 | -45.42367 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ce999a46-6803-36c7-bdbe-486dd9d5ea5b | -8.08463 | -45.33002 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 837df534-720a-384f-8964-5520cb0bdc01 | -7.87801 | -46.26242 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 469aa892-6042-3f56-9925-841208a58e2c | -11.19481 | -55.00745 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b8601bb-71af-3f2b-9f2c-97a3653eef7d | -5.49076 | -60.13357 | 2025-09-05 04:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3bc0043-5093-3898-82dc-85b423f81bb7 | -8.01129 | -50.09947 | 2025-09-05 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e81b1133-3ef4-3b95-b936-bea095fe35d6 | -10.08822 | -48.05482 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c000fee7-3f95-327b-af16-e7fce7b0c11c | -8.04883 | -47.56701 | 2025-09-05 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09f38f7f-1f47-37f3-af8e-7d80c07d27a3 | -10.7605 | -45.26946 | 2025-09-05 04:36:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d19a7941-fe2e-35ee-b462-b6a535432214 | -10.09602 | -48.07056 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 851171a0-5075-3b0a-b754-8e7b98aca5e9 | -7.68483 | -50.26085 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9ccff25d-d3fa-34b2-86c1-09a714e3602e | -9.00127 | -45.52143 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ec153b1-622a-302a-807e-853c4887db75 | -11.60039 | -52.16425 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc5a6a77-4a32-3c0f-b9e4-8b326b56e718 | -12.83671 | -44.44915 | 2025-09-05 04:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f0dfcf6-72ae-3b74-ad37-a87171ae15f9 | -9.07101 | -50.43598 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4f8e635-6623-34ec-836e-1a982eb1dea6 | -11.00683 | -45.94031 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ae26ddd-dd9e-3766-a96a-959f8ac1d782 | -11.57432 | -52.16415 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b8a27db-d164-3a1e-b015-ac15057dacf9 | -8.49577 | -44.62906 | 2025-09-05 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85c871ce-00af-3731-8504-01783dcdf17d | -8.18887 | -49.58848 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12701ac4-1737-3a83-9ced-5d15c030cebe | -11.91702 | -46.63867 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eb652a1-4303-308d-b9ae-16a4a33f65a2 | -9.42227 | -46.78397 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28ce9cdd-2046-320c-9694-e52236050ea4 | -8.20799 | -49.59903 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 006fe79a-09cc-3288-a6bb-504172c57f8f | -9.43936 | -46.80936 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e8a745c-8353-334d-b068-73c7e2dbd27c | -8.64637 | -45.74884 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c686f961-3ac8-39a3-b8ac-619d1e9e3dd0 | -9.42852 | -46.76593 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52563d51-4a2f-3def-a533-d1763e3ecebe | -8.19166 | -49.59265 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33faee0f-689e-375e-bab9-4f0f12a5204e | -13.44559 | -46.92974 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ef6efec-60e9-39ed-b3af-bd536b17d765 | -9.71433 | -51.08546 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56b47446-888c-33a3-8d02-966d22695ad4 | -8.93646 | -48.6472 | 2025-09-05 04:36:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README33.md)
