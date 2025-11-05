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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e8120da-56c3-373f-b9c8-cb91dfdb7554 | -4.4633 | -43.2152 | 2025-11-05 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| a6ff5b04-1ab5-3480-9d03-0e72ee1db90a | -5.0399 | -43.6205 | 2025-11-05 04:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 50d53e0a-c6b6-3a51-aa36-5b23bad88e39 | -5.4553 | -45.3988 | 2025-11-05 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 9bc41eb8-12bd-30eb-ade2-2b704096d0e2 | -5.4705 | -43.5906 | 2025-11-05 04:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 609cac70-8d89-385e-8b28-b4c2ba48484e | -4.4075 | -48.926 | 2025-11-05 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 265ed1ef-d666-305e-9fe6-47c66f222780 | -4.4073 | -48.9474 | 2025-11-05 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| cf57d2e3-5931-3dc4-8275-2f11114cd767 | -4.4632 | -43.2386 | 2025-11-05 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| a55cf993-c5fa-3680-b2eb-950e336df91b | -4.4632 | -43.2386 | 2025-11-05 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 1d55365b-8eea-36ce-9bc7-28288ed98a86 | -4.4259 | -48.9465 | 2025-11-05 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| ea1e7748-5e3f-36d7-8dd9-51bfff69552a | -4.4633 | -43.2152 | 2025-11-05 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e3aa07f2-dd37-3c8a-bb38-67fe8b887252 | -4.4446 | -43.2164 | 2025-11-05 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 902f4ec9-216e-3f6f-af76-775c49869647 | -5.4705 | -43.5906 | 2025-11-05 04:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 2fbe6e3e-02e9-34d2-a77b-494f46f09778 | -2.6509 | -48.4985 | 2025-11-05 04:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| b1c21c20-0f11-3fe7-9134-d2de0c76d229 | -5.0399 | -43.6205 | 2025-11-05 04:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| fd28314b-cab0-3775-9b44-c2074ff4b730 | -2.6508 | -48.52 | 2025-11-05 04:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| cf000415-a37d-3a76-973e-f4842ca329bb | -4.4073 | -48.9474 | 2025-11-05 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 8183c032-7c0f-3e8f-910a-8c09bc8987b1 | 3.40548 | -51.2861 | 2025-11-05 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e1ba908-db61-35ea-a2bf-dab361565627 | 3.36592 | -51.30058 | 2025-11-05 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cecf7bc0-ddd7-3c45-9ed6-f27d356a91be | 3.40552 | -51.28882 | 2025-11-05 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4327fe2-b4a5-388e-a9f8-2631980759a3 | 3.36531 | -51.29645 | 2025-11-05 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f7b752e-57b0-3f1b-a845-216079c6c9c0 | 3.37113 | -51.29556 | 2025-11-05 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5453be32-8a17-3eeb-adf4-f84e0b11c63a | 3.40611 | -51.29025 | 2025-11-05 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c58fb47e-25e7-39cb-9538-d79946691939 | -5.78529 | -40.82457 | 2025-11-05 04:12:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1c1aaa7a-a15e-3beb-9072-790db81b8eb1 | -4.61374 | -45.35186 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8797a793-4799-3998-9204-f5be38540b56 | -3.47875 | -43.63027 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0dc9dd1-e36b-3c04-a46b-33a37a85d245 | -4.33655 | -45.74682 | 2025-11-05 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b76bd599-0848-38d7-bdd6-b4bcd27a08b1 | -2.65244 | -48.51704 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3de505a2-ed14-3a3b-b011-5afe2321dd03 | -2.63699 | -48.50132 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dc7ffe9-5448-34aa-b1b8-525e86e63202 | -6.08089 | -41.78178 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 47c5ea85-d654-3dc6-9295-745443350d8b | -3.31562 | -53.84521 | 2025-11-05 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 730427c9-78b4-3da4-b182-6a111d2f4eef | -2.96393 | -48.59738 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e0c58059-911f-3371-a1a9-f918d6ea22db | -5.82203 | -39.20672 | 2025-11-05 04:12:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 82dec404-f56f-3cb8-b556-c91cb829613f | -5.14863 | -41.22468 | 2025-11-05 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f2f9bed5-8989-3daf-adde-a01dec4a93db | -1.21752 | -49.13766 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45d3e7b6-a707-3ee8-85b6-59f6672718d1 | -6.50346 | -38.21014 | 2025-11-05 04:12:00 | NOAA-20 | LASTRO | PARAÍBA | Brasil | 2508406 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c6904469-258e-3fef-b602-027beb18bb69 | -5.10765 | -46.21529 | 2025-11-05 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 490c298b-8937-3b2f-b930-99cffe54ec28 | -2.82097 | -45.14842 | 2025-11-05 04:12:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 8d8eeb1a-8dde-3626-a781-b4dc33531fab | -2.44512 | -49.03396 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8073c11c-4992-35ee-9156-c3bfe77e6114 | -3.22948 | -43.44226 | 2025-11-05 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 340c8f90-afdb-3dd8-b7ac-07fc31878daf | -4.11183 | -48.01844 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 82e0c207-ee2f-3557-9f1c-62cdf6c52910 | -1.2849 | -49.15118 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0fc5a3e2-44a8-3577-be40-7227d4dde66f | -2.82348 | -49.41857 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d3b44e4-14b8-3ce3-934c-e7b7abda4353 | -4.86345 | -44.62635 | 2025-11-05 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db407641-e5da-396d-9acc-e55f80797ed5 | -5.0583 | -45.82872 | 2025-11-05 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12068672-2434-3e79-8e99-9d7a0b0e0248 | -3.76549 | -51.71307 | 2025-11-05 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dd86bbf-951c-3cbb-8e13-c324da26039f | -3.48379 | -43.62018 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc1fafb4-dde9-3bb1-80ed-3a1a690f2e74 | -4.23924 | -48.6657 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf8499ae-efc5-3e5c-9f0c-09333239abb5 | -4.47201 | -50.90572 | 2025-11-05 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10fd0086-0904-30e6-bc60-927fa0822748 | -1.28021 | -49.15042 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 10ab526c-e568-31e2-96c3-a2679c049836 | -2.72912 | -47.38609 | 2025-11-05 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f54da851-c8df-3e4a-826b-a1ff47404809 | -2.65455 | -48.50417 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1b6a31a-9bfb-372e-b6a4-8e62f471d993 | -4.55834 | -45.78805 | 2025-11-05 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 017749ad-7d00-3bb9-8121-caf354c1e4c2 | -4.35671 | -50.88771 | 2025-11-05 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 998c5c19-4492-33c1-8322-c3b9566cd552 | -3.07299 | -52.63369 | 2025-11-05 04:12:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66a3b3d6-b05c-3b22-889e-ead4fc1f1e1c | -4.71447 | -46.44012 | 2025-11-05 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 546764ff-6423-359d-8fc0-22f7025396b0 | -3.31397 | -53.85492 | 2025-11-05 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b07653f-ec73-39d4-bead-ced0452d0add | -5.21056 | -44.45046 | 2025-11-05 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5134912b-fe56-3264-aac2-76bb50dceb1a | -5.9917 | -42.95479 | 2025-11-05 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0d6db1e3-b674-3fe8-998f-527e0d817119 | -3.50195 | -51.55608 | 2025-11-05 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0381520-acc9-3016-848c-463a1bef2535 | -3.47988 | -43.6232 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e8594ee-f97b-3ec4-86a4-0c9bf08e38e3 | -4.45547 | -43.21369 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27cc73a8-99ce-36ae-aa26-a1372b7d9558 | -2.08142 | -48.36767 | 2025-11-05 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e11d082-1c4b-3aca-9961-4d51e71dec03 | -4.46431 | -43.22218 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a5c8f215-aefd-36d2-be57-6307be2469fd | -4.152 | -46.79419 | 2025-11-05 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 998dbcc9-081b-316e-8e32-db1c947be30d | -4.46597 | -43.23309 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2ed1c91-dc1b-3292-92f9-18d6a0beb7d4 | -2.1025 | -47.34205 | 2025-11-05 04:12:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5458c805-cc5d-3599-94c9-8492a53d880c | -4.4516 | -43.21663 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 2f287154-8e34-333a-8275-9cecf8fe462f | -2.97714 | -48.71031 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b66df6e2-e70d-3a2e-b56d-2fef4a950113 | -4.46652 | -43.22963 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| fddb20c8-988b-323e-b21a-5a79ece2bf50 | -5.14527 | -41.22408 | 2025-11-05 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7a75dd8c-21ee-3e5c-b59e-b11732482d2e | -2.95953 | -48.59666 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aba5d0db-1f16-3a10-84c7-48ae5aafc9de | -5.51485 | -41.14355 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cff1b09f-e286-3cd9-ae55-9ecd04a62a9f | -3.88123 | -42.52575 | 2025-11-05 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 74a85ecb-364a-3aa7-9c08-34ee3392bbc0 | -4.91759 | -45.55849 | 2025-11-05 04:12:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 682ee7d1-46bf-3579-b4a3-c5e44361e6dd | -2.29239 | -48.51073 | 2025-11-05 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1baae2c7-ca7d-3740-948f-740e7423eb27 | -3.8889 | -44.62429 | 2025-11-05 04:12:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72117dd5-1336-3876-ac73-d2fbfc603528 | -3.24103 | -50.79709 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37062f27-2dff-3d45-8fdc-db37404e7422 | -4.7627 | -42.64774 | 2025-11-05 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 47.3 |
| 4e0f864e-ef21-369d-af34-03b1c1c33caa | -3.79274 | -44.04243 | 2025-11-05 04:12:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ebdbf0e-479f-3c89-914c-1c449ae0650e | -4.90526 | -44.75859 | 2025-11-05 04:12:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94ca3353-5dcc-3aaf-bc48-90e8862aa808 | -5.52844 | -41.14555 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6f307c58-bbde-3d84-aa03-13f9038dc3ba | -6.58659 | -35.25478 | 2025-11-05 04:12:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 203756b2-f590-32dc-908f-068b1d218a99 | -2.83279 | -49.42016 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fafc7ad2-a1c4-3889-8351-35578bcf5ebc | -4.45492 | -43.21715 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| cde7c41a-2c24-3247-9b91-e605a07b96c6 | -5.53077 | -41.08611 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab6c5e3c-251e-399b-8d16-cfbf983c640f | -3.06928 | -47.77563 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d7d43a0-fe29-3b06-bb50-ba8e0910642b | -4.02858 | -47.95521 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e35f5f04-2c51-3579-a986-b18439ded721 | -3.57074 | -50.6414 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4e2e46be-868e-3f8c-ac8a-05841c30e9d7 | -5.42194 | -43.46301 | 2025-11-05 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f3c0842-3924-3d24-8b9d-467a10bd2a8e | -4.86627 | -44.63064 | 2025-11-05 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45896997-c139-3c3f-a331-6667b5f07cd4 | -3.06864 | -47.77947 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7004481f-482a-3187-b04c-0589f18178c7 | -3.4916 | -43.63593 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00883a48-ad9c-3d4f-8b59-d1249ae53aa7 | -4.5501 | -45.58817 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 15337c83-3e62-3124-a67c-a8995c33d30c | -5.92646 | -41.291 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a58f1452-3b82-38e8-a3af-84cc17488fc7 | -3.32182 | -53.84629 | 2025-11-05 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49cb9813-924a-35c7-a13e-f4698170a21e | -5.92567 | -43.37237 | 2025-11-05 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4fb66c17-d168-3dc3-85f1-0647a8bf1242 | -3.48433 | -43.63842 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aeebc0c3-4716-3358-accb-1d062d234f6e | -2.84453 | -49.40702 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3fc77a8-0854-3e33-9790-e443672513b8 | -4.71652 | -49.77025 | 2025-11-05 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d86d5fc-33c8-376e-8eac-9ce836ed9390 | -4.55075 | -45.58416 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README17.md)
