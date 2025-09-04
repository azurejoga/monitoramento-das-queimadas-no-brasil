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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64cad892-ab5f-36ae-b77c-d1d9d34ce9ac | -7.69526 | -50.26292 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b6fd7cd-302e-3bdc-b683-62fda8894692 | -6.22726 | -43.56005 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ee19954-39b5-3e69-944e-8086dbc866f2 | -6.78371 | -44.45885 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 864bf8f9-0e4a-3232-8e58-5af6048b5d6a | -7.14478 | -46.75302 | 2025-09-04 04:53:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35088979-b974-3db0-9eb2-6bdaf4d74cc7 | -6.22692 | -42.43761 | 2025-09-04 04:53:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97dd343e-1cbf-31a8-833f-e2c3def65392 | -9.48838 | -47.61557 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d80fcca-bfda-3361-a795-e84669fa7124 | -9.71756 | -51.05273 | 2025-09-04 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54be1612-c5ff-3ea7-9cee-88a4cde85f47 | -5.93486 | -51.9721 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fa36211-5228-3143-a080-a230dbf3dc51 | -9.33794 | -55.2119 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f85166cd-98a1-35d5-aeda-44ba0efa8e27 | -8.07924 | -45.34348 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb71848a-b9a4-3aef-b306-dc345532fc4f | -6.25121 | -43.2962 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0124c67d-de2e-3cde-adaf-be77b5724920 | -7.7153 | -50.32147 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4b6ae5d6-0666-3857-b656-b9e237174e65 | -6.76622 | -59.67356 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ff83cce-98e9-386c-8e2d-42e6a026ecec | -7.51049 | -45.37254 | 2025-09-04 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef927189-bd5b-34bc-a272-3b9f8b86e183 | -6.73505 | -42.26065 | 2025-09-04 04:53:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7acb63b6-997a-3e84-8ede-b224a9a9273c | -10.03516 | -48.15077 | 2025-09-04 04:53:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a16dec1a-48b4-33c2-bd19-7a6a1d629289 | -6.41372 | -43.263 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b468d33-635c-3af5-acb2-b2fa7091be20 | -9.75701 | -48.99919 | 2025-09-04 04:53:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7a8930d-9338-3030-9aaf-c2f77bd79d63 | -7.36845 | -44.32484 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05c09381-9ab6-3143-937f-4bcad7dc0877 | -6.75763 | -63.1344 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c93cf58-e8ee-3b99-b07f-bbdd5952831b | -10.0333 | -46.08873 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f962451c-b90a-3989-a32c-8f1175c1f5a9 | -9.60786 | -47.03073 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 553015c5-f255-3b9a-8d55-e7111736a8e9 | -6.64731 | -44.09702 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d093e9e1-557a-342d-91b2-607cb86fcc41 | -9.61166 | -47.03567 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d95a0805-9be2-35fb-8812-d9112e9d7ae1 | -6.28268 | -43.84877 | 2025-09-04 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 673192b0-4e10-3c1d-9866-be8bc8818cb8 | -6.75351 | -58.72614 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 872d1223-99e5-3687-b1e4-f3ee5de8e2af | -6.87808 | -59.98826 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c40e5ba3-6a1e-35ff-b30b-210790b055fc | -6.46267 | -55.88638 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ac3baf3-2bc3-314c-9d67-7294d745b2ca | -10.53368 | -46.76252 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6554be4-6e91-3623-b9f4-45ebac15d10b | -5.69523 | -45.17238 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0be1fd6b-2d63-378a-bdb6-7f5f7d04e1b0 | -6.76241 | -59.66804 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 822b2da6-d72b-3b73-bd21-cc62b5a13efe | -6.5019 | -43.07289 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4581a19-f17f-34ec-826f-52fa494082ff | -5.67016 | -53.74502 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee20a891-2c3c-3c78-98c0-c27a4be8aa71 | -5.60915 | -45.02384 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8ffb1a0d-816d-36ad-b1db-6e8510bb1fe6 | -7.70591 | -50.28796 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39a72c53-db88-38a5-89f7-ad79fc64c7e7 | -9.04179 | -47.0178 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31f542bc-f630-3725-a357-8e3e79fbb791 | -8.37501 | -48.32819 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f8be161-b5ab-3108-aabc-f54ac7a0e6f7 | -6.0855 | -43.28362 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d8e049a9-927d-3981-8451-b21f63d093d7 | -5.92417 | -45.55173 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dddef92b-a99b-3297-8285-342b5fb105a9 | -7.27231 | -57.56188 | 2025-09-04 04:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa87c76a-68da-32c6-b74b-5d9aaad5eafb | -7.72 | -50.31414 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| af582476-d6e4-3730-8b18-532fc976fbf2 | -6.12147 | -42.94675 | 2025-09-04 04:53:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1b1cea45-ced0-33b3-bee1-aeabf95cea54 | -6.20029 | -43.34501 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d5a47a8c-fa7e-34b4-918c-af41e59ab59d | -7.05514 | -50.86455 | 2025-09-04 04:53:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70e23922-8ace-3b7e-aa3f-417f1e4a0bba | -5.31763 | -55.8564 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab7a6b6d-5d90-30db-b2ce-498b1161df58 | -6.288 | -43.51296 | 2025-09-04 04:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c15783c6-a2c9-31e1-8374-4cdb77855805 | -9.70735 | -48.95526 | 2025-09-04 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d9d16090-1800-319e-a624-d2b1e2918de8 | -7.68635 | -50.27388 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d1c2384-1011-389b-8176-675efcaeb3cf | -6.24799 | -42.63834 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f06039d3-3057-3cc7-ab41-277af48d677f | -8.03966 | -44.14076 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a2dd905-5b09-3bce-b96f-25ca724967c1 | -6.70004 | -48.41455 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4ca99ea7-c23a-3704-b0ba-52b5989a2c4c | -9.57183 | -48.23757 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6c23a991-2452-31cc-aba8-3ca47f0d7d15 | -7.74503 | -48.76653 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a797afa-713e-369d-bfa1-1fac4132771b | -8.02921 | -44.13928 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7d0b9a8-7ae8-34a1-abcf-b8ccda22e0b2 | -7.36802 | -44.32789 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c3c9cb4-8252-3028-8210-4d29272ec8ef | -7.36378 | -44.321 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46840d7e-6c93-37ab-8f9c-104b9155b6f3 | -3.98468 | -54.20874 | 2025-09-04 04:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27de56fc-2533-354b-9883-314f054480b6 | -6.46863 | -43.97535 | 2025-09-04 04:53:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc6bdf76-787d-3e26-be83-4ece6490596b | -10.12616 | -46.30007 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5271d61-5bde-381f-a117-8a9a6e9e9c55 | -7.72746 | -44.62442 | 2025-09-04 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1aabef29-25b5-34ad-af3e-35dd895bc66d | -11.03527 | -45.13692 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 30a97734-29ac-3244-9fdd-f34802cb8f14 | -6.12542 | -44.14421 | 2025-09-04 04:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c999ff28-ab4c-3e31-bc81-b3350fc8d854 | -6.67049 | -60.02831 | 2025-09-04 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3afccf07-d524-3f5d-a673-6683ade04f55 | -6.16598 | -43.3158 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bedcc5f-062a-38cd-8c00-559266d0b8fa | -6.61845 | -43.96573 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf42b447-4432-3ff5-a916-c5e2970dd19e | -6.24959 | -43.55492 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 853fe12e-edc3-326c-a685-509948f1ba80 | -8.8553 | -52.01588 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77e1cb57-fa14-3c64-890b-d7eab6294f0e | -9.97165 | -51.62806 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63e7527e-75fb-31fd-a1e7-52059e998013 | -8.09009 | -47.58895 | 2025-09-04 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73fc8ff9-6752-349c-abe7-f875640b3aa1 | -7.36574 | -49.39749 | 2025-09-04 04:53:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b6d028e-159b-3f66-bba9-f03094096b31 | -7.68285 | -50.27322 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1fbe204-7da0-3193-b797-6b30344481e5 | -9.4679 | -47.60859 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b084abb-1ae5-3b81-9d58-fba2f082f6da | -10.05548 | -46.06639 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 792b353f-9112-3cb9-bcab-aea414877ce9 | -6.30414 | -44.15195 | 2025-09-04 04:53:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 630f669c-b25f-33c0-8f5e-febfb24dd974 | -8.3617 | -48.33639 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 259a4302-1900-35d8-ac34-c52dec5ab087 | -6.29438 | -43.50623 | 2025-09-04 04:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6f11674-1973-3064-8b4a-de700afd946a | -6.79196 | -44.43674 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10da5551-8533-386d-8d3c-a861dfb86ac6 | -10.71813 | -48.37306 | 2025-09-04 04:53:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33d8f7f3-dc78-370c-8932-8e188ec28d27 | -9.33106 | -55.21072 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6000318-b83d-3ce1-b441-0c5f2e4bc7d3 | -6.22623 | -43.54369 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6e04416-343e-3aad-8014-a97b5901dd36 | -6.25212 | -43.2999 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2596bbe4-16b0-359a-afb8-d753671aca56 | -8.19455 | -49.60098 | 2025-09-04 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87baac24-f506-3be4-b9ed-e16d0c9ac83e | -7.7613 | -50.73121 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce6a73a4-e9e4-379b-9754-adf4365c0d16 | -8.52983 | -51.31684 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bb80a7a-f35d-36ac-a7cc-e364bfd0fed7 | -8.01876 | -44.13781 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8259d245-f384-3417-9662-ae89af0e5560 | -6.23978 | -42.61417 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1b587ec8-e3eb-3f5d-8c5e-efdbaae5908c | -6.02647 | -46.67728 | 2025-09-04 04:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b25d3b4-5ecb-3ddc-b5d2-f1ca9522cda1 | -6.78369 | -44.0855 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 66c3ccc6-b9b2-36fc-8ee3-5e0c052a9ca7 | -6.77234 | -44.50319 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be1dfcf1-77bb-3fd9-b361-6ac78610d608 | -6.80874 | -44.46299 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0521bc87-cbdd-3bd3-b46c-88cdf15db535 | -6.03625 | -46.00264 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 141ec73b-c1a8-3c9e-90b7-b4905c9f3e90 | -9.61604 | -47.03632 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af4fac76-be2e-3032-bbc1-165271ddab67 | -9.6526 | -48.04176 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd594f6b-6d51-3961-b6dc-b2bda25d886d | -6.59523 | -44.31673 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bf7d2dd-5e98-3f74-a59d-4a125279b967 | -6.21593 | -43.389 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0996520c-7ac5-38b6-af49-4a7ea91948bd | -10.65257 | -44.8409 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 082576f0-533f-3ccb-9235-92bffd0e1f62 | -9.43098 | -48.09648 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 55f15ea1-52d9-3756-b9a8-4b950ba2eb30 | -6.12157 | -44.11757 | 2025-09-04 04:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b1d5c70-4328-3eec-94d5-7cc5061ac29f | -7.34712 | -48.18806 | 2025-09-04 04:53:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f35f37e-99dc-385b-bf7c-a142423aec07 | -6.75738 | -63.12812 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README61.md)
