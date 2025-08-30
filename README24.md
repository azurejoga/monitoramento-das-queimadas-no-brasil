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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18af96ef-a958-3e29-9401-b65bcc227865 | -7.12093 | -44.59932 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1538a446-2ed4-3010-b91f-3406593dca65 | -4.88142 | -45.51617 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b5dc438-17e1-37c9-861e-fc2ac16e4c6f | -6.36232 | -43.56914 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 66fd428c-df2d-3432-997d-293ce965b3a6 | -8.44777 | -43.64682 | 2025-08-30 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dc9a519-f44e-3f32-8dc6-6071e84ee758 | -3.28816 | -43.41714 | 2025-08-30 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 592ac7e9-d3e6-3e36-a110-07cb9a2ac48a | -6.2324 | -42.40506 | 2025-08-30 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a248147c-3e88-3c56-abf6-16a9668f1191 | -3.07154 | -49.45903 | 2025-08-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dc89589-6ba1-3bd1-8964-46e596a074d3 | -7.3951 | -45.92949 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 362a5f42-ffda-39d9-984f-874f984b3302 | -6.16583 | -44.2006 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd473bf1-71ed-3a6a-8497-974e820a42a6 | -8.45687 | -43.64074 | 2025-08-30 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6a146ada-1cef-34ee-b13a-5e427bcba8b7 | -4.37328 | -48.06784 | 2025-08-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42a8fe80-f799-36c4-b622-92c447501079 | -7.78078 | -45.46968 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 835b33d2-60d9-3667-a7a9-05076b58844a | -5.67336 | -43.44858 | 2025-08-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec25020a-6fc7-3331-bffe-988beb8632ec | -4.89941 | -55.84849 | 2025-08-30 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e52dbf3b-bd82-3625-88b6-3b44f2944f2b | -7.57864 | -45.13282 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 82ad130b-e775-354c-a6df-30116ccc729f | -6.70567 | -43.0945 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09f0450d-699b-36f0-aa9f-1a0e281d6db8 | -4.79404 | -47.2648 | 2025-08-30 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c02534a-7ed8-31e2-9c7f-f42db5c56ce7 | -7.80928 | -44.8073 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f4d85ed-858e-35c3-9f92-4f2f51859477 | -6.28153 | -44.46395 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be2d821a-1619-31d6-80e3-4cda2d470082 | -7.1095 | -44.58333 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4ed72a6-67ef-3972-a20b-12c335837d39 | -6.87636 | -44.44344 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d9873c4-fdf7-349a-b0b0-bfffa5d4df56 | -6.18572 | -43.32598 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5cab661d-51d5-3bab-8a09-d602ea30b114 | -5.25469 | -36.91227 | 2025-08-30 04:19:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3df10b25-8bd8-3a53-86d9-039324ce585b | -7.09667 | -44.53518 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31e372b3-f35f-3a20-9472-6b137694953b | -6.69315 | -43.08508 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c2b9b31a-4ada-338c-a6bd-46cf44f76f4a | -6.59113 | -43.65191 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1e4aa57b-87bf-3799-9959-7fe24d117df7 | -6.04999 | -44.46622 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4bae5ae-0eda-3bd6-a385-2901745c284a | -6.52279 | -44.85513 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0e654ca-40af-30fa-9fb6-c183ae030aee | -7.63911 | -46.55844 | 2025-08-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af4848ec-0185-30ac-8b0d-9aa435d7e9c9 | -7.1646 | -44.16365 | 2025-08-30 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00368592-06d7-3cc4-80ee-186871208631 | -5.40398 | -43.34536 | 2025-08-30 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f069a2df-aa81-3e40-85c7-7f6cc375780b | -5.90002 | -43.38872 | 2025-08-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a696ce21-cdaa-3eb4-945b-886dfdb84f23 | -7.39454 | -45.93301 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 13c50699-34ab-328f-a132-1b5dbc30d716 | -5.77585 | -45.38872 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 30432306-2ea4-31b3-9ea8-087a173875d3 | -4.87815 | -46.84947 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b11a791-9427-31a3-a6bf-582d7f25a6b1 | -6.48567 | -43.54101 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47c45c23-478c-3e30-a0c3-913ea3910440 | -7.64741 | -42.65725 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa62e689-af51-36d9-b3b3-cb36ccfd76b5 | -8.05409 | -45.41752 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| adad0448-dd00-3300-a50b-8b4daf3f9d8e | -6.21019 | -42.75487 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5295fe15-e685-31d5-82a0-df602ae384f8 | -3.21719 | -46.82777 | 2025-08-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7bd6b4f-0ab6-3655-8ee3-45b5cf311ffa | -5.81927 | -46.36273 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 546e1b69-1515-315c-abfd-7ade472a60ef | -7.63969 | -46.55483 | 2025-08-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a42eed76-cccd-375a-8862-14e6fec7ef88 | -6.50915 | -43.54477 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c18b95b3-81d3-3945-ab5c-56ec567d5285 | -3.85304 | -48.98653 | 2025-08-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 40a4b95d-06c4-38f5-b033-02a5168fd287 | -6.17449 | -43.33166 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6bbba60-a1bc-3ad8-a029-1b5acee240b9 | -6.00411 | -44.71694 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18c976fa-63bd-354e-b49e-bcf7a126f1c8 | -3.73916 | -49.0445 | 2025-08-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ecd3fd8-300b-3b4e-81b2-83ceaec717f7 | -7.6073 | -44.9495 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f11fac5f-675e-30cf-a7cc-747ae45516d0 | -6.09217 | -43.99667 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2797ec84-c31a-35e2-b2e6-9c3549a4e0c6 | -6.64127 | -44.24977 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9af69f20-be0e-3f49-8b9c-134b1625d289 | -8.11139 | -45.00782 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e73f50d7-deed-3f55-ab59-29b5627d7007 | -7.40377 | -44.28718 | 2025-08-30 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b44b88ab-656d-30eb-9b72-a66e4e264fa2 | -7.43197 | -44.80801 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4f024431-455c-3495-b76b-0ad09ffe15a3 | -6.17505 | -43.32806 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcb1b172-448c-3f68-b89d-c2a6095e22cf | -6.8033 | -43.7312 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a00bd521-fe42-3d58-af5d-dca93aeefa43 | -7.22161 | -45.43423 | 2025-08-30 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6da4f8cd-61bc-3f25-80c0-979b70f9e2b5 | -7.60626 | -42.70699 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7886869d-b459-375e-ab3f-4984b9fb1f91 | -6.86866 | -44.44936 | 2025-08-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2492d27f-d9d2-3980-8cee-c7b59e7ffe6e | -2.42784 | -47.23623 | 2025-08-30 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80aeca0b-bb90-3855-89d6-49c6ca67c558 | -5.85857 | -45.62032 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d57f0e7f-7626-318a-83d8-d59c7dddb017 | -6.42525 | -44.17365 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 12d7b1ac-c2e7-3a18-acee-698478391007 | -5.86945 | -42.89806 | 2025-08-30 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d7042d2b-a2a0-3830-953c-2994cc25c2fd | -3.4254 | -49.04479 | 2025-08-30 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d11fea06-5d03-3d46-8e9a-faa4f6da9356 | -6.88684 | -44.44149 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcf95674-f535-3ce2-aeee-fbc1e9b70202 | -7.34947 | -47.53064 | 2025-08-30 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 352209a9-5288-341f-8eef-4451a224bf64 | -6.93469 | -44.35272 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec6516c9-1336-38f0-91a8-d9e06afda902 | -6.82441 | -43.05154 | 2025-08-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99956efc-e86a-3d6d-adda-0efe26634e1a | -6.19669 | -44.0021 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16f40fba-3fe2-3478-a8b4-26d62c4611b1 | -8.4817 | -43.63716 | 2025-08-30 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7793c781-2460-37b8-8e1f-6e0fe4f74ee7 | -7.42429 | -44.81389 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffbde009-3e46-3f51-8ca2-17cbf2dfb17d | -7.58886 | -42.70428 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b3c16990-2417-34a5-8666-4ac1be2f7916 | -6.06697 | -44.44408 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 212b6ebc-9d8e-3c70-8c96-210b32f4ca4a | -6.37808 | -44.34416 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c1cb472-81e9-3979-ae1e-2fb5ec94f2d7 | -7.11762 | -44.59879 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c0baa7ef-42bc-3a11-810e-94511d8625bf | -8.05794 | -45.41457 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4d5fd0dc-e891-37d7-9e5c-4b8f51c182b6 | -6.41285 | -45.60044 | 2025-08-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a2310af-73c6-3dc4-ac9f-f274e42e7d37 | -6.39615 | -45.2527 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09524216-83a1-3003-b30d-34a41d653bcf | -7.11816 | -44.59533 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 55f94483-ed0a-3c24-89b4-2e202f349203 | -6.39946 | -45.25322 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8429cbdb-5c5f-377f-85ab-ae694a4f1d4a | -3.73583 | -48.94005 | 2025-08-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6af1faf-e386-3830-8de5-91c8fb8d7534 | -5.96056 | -44.51583 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 617866b5-28fb-3a04-a751-aa7ca77135c2 | -6.20963 | -42.75862 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 99592654-ae6a-31d5-80c7-b7a8ef6818b1 | -6.52457 | -44.86951 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc69259c-cdfe-3a05-9b93-dfba57b33ae9 | -7.6033 | -42.72638 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9922dce1-07cd-38b3-9dc5-75bcf26e01c3 | -7.54395 | -45.35421 | 2025-08-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55a17853-b79f-3720-a9a7-2e2c38e2c28d | -7.40893 | -49.51939 | 2025-08-30 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 027a98a8-006d-32c7-b9c0-87cf2493680c | -6.52921 | -42.96277 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22ed7005-d12d-3df8-973a-314af98e87bd | -4.87058 | -46.85235 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75cc83e0-dbff-356f-99c5-663beb935ce4 | -9.49903 | -37.96256 | 2025-08-30 04:19:00 | NOAA-21 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 59a14b10-5258-3e9f-a7a3-409ddd93f11e | -6.40219 | -45.58094 | 2025-08-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e173fa70-ea36-38f4-b851-1eec3a0bf438 | -5.04573 | -37.99979 | 2025-08-30 04:19:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 407e3912-5e68-3a99-95ea-de6efa22d8ed | -6.17731 | -43.3358 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| cdc9c769-b797-3577-865b-44ebf3f8d25f | -7.72044 | -50.3003 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ee1ee39-101a-34fa-a15a-3d6285b18396 | -6.17227 | -43.3461 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 256aac35-e23a-3553-9659-ede5af614889 | -5.96109 | -44.51238 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a512735-8e73-353f-b7aa-6728c0068b34 | -7.60159 | -42.71423 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0071155b-d266-3271-99b3-7edbf56b5c0f | -6.57224 | -43.68541 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 691bdf7a-0cdf-3140-bc2b-6a39db35ab4c | -6.27876 | -44.45997 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51896274-1c21-3854-8ff5-b7c2d7010309 | -2.44308 | -47.33233 | 2025-08-30 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 069761cd-707f-35ba-8aa0-2a35393a672d | -6.49518 | -43.54621 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README25.md)
