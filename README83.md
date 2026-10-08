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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fef43d3-590f-37b7-90db-963c8927150f | -2.98564 | -54.13233 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eb624b87-d67c-3778-8788-84b782c1c5b7 | -2.4771 | -56.10512 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 111d7c8c-6495-386e-a3a7-ae67210fc47d | -3.08043 | -54.29071 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 41dabe79-dc7b-367e-8870-a049fb9c46f1 | -3.03992 | -54.23413 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a4af421-965f-34a0-a229-9361665ddcef | -3.00283 | -54.07213 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| baaacb6d-ed83-34fd-b88e-cb20d975eb33 | -3.02218 | -54.23764 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35101c3b-3d11-3a1f-87c1-f8794c2ff6f8 | -2.96129 | -54.14218 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b757874b-fb5b-3268-bc85-7414aa5c64e7 | -3.85724 | -55.9809 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8adb38b5-26f7-3681-812b-b2f3e2e1cfc8 | -7.07081 | -40.94068 | 2026-10-08 04:46:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 93c2c41c-dcf9-3f07-b65b-2af13f0ff8db | -12.04304 | -43.43737 | 2026-10-08 04:46:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08515ea2-f8e4-3bc9-9114-aa3b3188ccae | -10.77737 | -46.55534 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db1aa2ac-ebdf-3c96-8d79-5c23db136703 | -3.14458 | -53.72582 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd19a878-0490-31df-b94b-098449c1ae29 | -3.16967 | -54.73187 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2297db23-6a64-31f0-b59e-196b5842d427 | -9.16797 | -61.40861 | 2026-10-08 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b976b20-884b-3eab-8725-0e701d76c34d | -2.9964 | -54.18388 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15f957d2-d1f2-34f7-9ec0-a2b22f8a22c5 | -3.57786 | -54.67765 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ed9e5996-13c7-3bff-afd8-414ae5756058 | -6.10479 | -55.71267 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9dda58f-1fc5-3fa1-9344-08005d3e40e9 | -4.77551 | -55.73659 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4be6a50f-c9c3-3e7a-8513-b832759f1cd2 | -4.96256 | -55.11903 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b35769be-a3bd-3296-b734-03f5ca66574c | -2.57401 | -56.17698 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fc74ca52-02c0-3e01-ad63-0846619870af | -3.34945 | -50.47707 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| b3103736-30d2-30d2-be07-65b608fada26 | -11.63261 | -43.69645 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 511fb0d4-8a19-32c5-9c27-aca1879a7939 | -6.37813 | -42.90248 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 27ed4376-f9f1-3b3d-bfbb-61bc2af7fb0f | -3.70415 | -61.32901 | 2026-10-08 04:46:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f772447a-1ab8-32f2-994b-9b1cc3247d4a | -10.44473 | -47.27851 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f937262e-7a29-3e09-a166-4d5d366deddd | -6.01091 | -53.52924 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 064485b2-db1b-31b3-80de-cff6575f90c7 | -6.11582 | -51.73883 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bc01d9d-9b84-37e5-a1dc-f5b9141f0dda | -9.80279 | -48.92128 | 2026-10-08 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c81c66c1-722b-3b3a-8245-cd3dda5c28ec | -2.74886 | -54.03964 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bf4763e-44d0-3279-975e-19faa4a464c7 | -3.33841 | -52.51322 | 2026-10-08 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fa6219d-883b-306b-b945-862f3b8caa76 | -6.10316 | -55.72253 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| faa4dd90-a185-3a04-97e4-17820873dd0f | -2.47898 | -56.09337 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a793db45-8a78-393b-9577-3ceb482ab0c7 | -3.00715 | -54.14014 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4509312-fb28-389d-9034-2ffe00a22fe0 | -3.54904 | -54.66359 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c72f24cf-ae39-3839-8d8c-8a4ebccbda3a | -6.84963 | -41.76879 | 2026-10-08 04:46:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 721c0739-236c-35e5-8107-0e8060ab534d | -3.96809 | -55.83865 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c377580-1156-3fc8-997c-7c546b19a3e4 | -3.32761 | -50.17854 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5165c738-edbe-3f29-9dab-2048a60861dc | -4.57046 | -54.952 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bf175c86-e031-3486-af48-e1884ec1eb82 | -2.93497 | -54.14879 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 763cf1fa-94dd-340b-8a0d-0b8dd4fe8df1 | -3.47524 | -50.0858 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1b9f143-ee52-3715-8fd3-b1a7ca9ed431 | -3.3654 | -50.48304 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee561cd9-2f84-3dff-b224-1f66a40dd58e | -5.69907 | -53.48116 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 642259ce-963b-3620-8ef8-99d750ebb3ea | -3.67836 | -55.95222 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99ad6523-faae-3b9a-9815-37e406a0b254 | -3.03926 | -54.10473 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 37199ad0-5308-3946-bea0-b28be810f45a | -7.20247 | -55.13469 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9464ee48-5324-3e2e-a6c3-3fcd85d55e36 | -11.22455 | -45.25151 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fd6615d-818b-3336-9263-77adc2737582 | -3.78497 | -52.35725 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 751781f6-b87f-30f1-be4e-b2aa776262b1 | -7.88491 | -44.24512 | 2026-10-08 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 996535af-c608-368f-9293-c8ed0b011fa8 | -5.07535 | -48.40936 | 2026-10-08 04:46:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f04bd8e-0482-3151-9467-220600a1052c | -6.17994 | -52.64776 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a64ab9c3-1c65-3773-8e18-9b5e0ffc4479 | -2.85714 | -59.11475 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fd4cb9e-b26c-368e-8d7d-24598d9ba2a4 | -3.52788 | -54.67427 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5683d96b-75fb-303c-86ff-5851cf12462c | -11.64922 | -43.68903 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f727434d-c4a9-3f3d-a409-a13cfc654a1c | -4.11361 | -54.02247 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0f15987-f275-3e9b-bc08-cdb967c882db | -10.3248 | -46.61343 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d749d843-704c-357f-bb25-0d5788bd162a | -3.2828 | -54.00985 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e233ac9-e20e-342c-aa1e-35fb3485d600 | -5.75216 | -42.05752 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a41baa7e-0b00-3384-ad47-342fda0d2a88 | -8.71997 | -45.17712 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bf86927b-8941-3b73-9039-2432a8c5f07b | -2.46648 | -56.06351 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0a59524-2b59-3c4c-a0f8-95e252601225 | -8.38981 | -46.30323 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d9787e11-6ebb-37c0-8631-6c6b99926c3d | -2.9667 | -54.17932 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 164c2846-d290-33ea-a151-6ea70fdfa6a6 | -3.5952 | -54.66626 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3dd42e9c-ccfd-3350-9018-cbd52282de62 | -11.37608 | -46.66283 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c01d711c-93d1-333b-926f-7aead1376280 | -3.11274 | -53.78526 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d48a7f09-fd95-3886-b88f-1ef53c756a83 | -8.71242 | -45.19863 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4bbfc5b-68ec-3e0d-b402-c07e37dffbf9 | -2.84442 | -57.48698 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d9fc3278-8cec-31cf-b99f-75e0d6374b8a | -8.06004 | -44.80771 | 2026-10-08 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9a840fd5-3869-3388-99b1-49bf73ff4de4 | -3.48564 | -59.45768 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c839626-1daf-361b-a472-c5bcee816baf | -3.08241 | -54.25444 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22707bb2-3b41-35ce-baa2-ddd05b8a9c47 | -4.20188 | -55.63134 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fac05727-ddef-3d05-b333-7856d173d7c3 | -6.67338 | -55.08909 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| da9777f6-dd93-3390-8c74-6350adf63a64 | -3.04957 | -53.92006 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d852853e-f79e-3672-9073-e720271f74c2 | -3.35658 | -50.47466 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dca7cd9-c143-33b9-ba6e-364568c08f5e | -11.09583 | -45.6608 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| deede88a-40e1-303a-b22f-25978a3c511d | -3.17282 | -58.62867 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51dadf09-1c16-384f-9324-89dccac524a4 | -2.99596 | -54.04428 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92c79399-873a-3617-94c1-4dc40dde7114 | -5.30102 | -45.54285 | 2026-10-08 04:46:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55be7a5f-533f-389e-af4f-96c4f63ea174 | -3.07884 | -54.27675 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f2370657-9e7c-3569-9281-9d8cbb957a6b | -8.37087 | -44.75941 | 2026-10-08 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56672f60-106f-3c99-8a8e-35a8fb2a10aa | -7.21076 | -55.17726 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1992a4a2-0ac2-363d-9aba-e3163c237020 | -11.22425 | -45.2524 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8ec8068-0d90-3e80-830f-de10ed847469 | -9.45743 | -44.61993 | 2026-10-08 04:46:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c1f8345-74ea-3e15-9cfd-c15afac963a7 | -8.60267 | -45.63696 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1389d901-01e2-332f-a265-27aeed1f4a95 | -3.29989 | -54.04341 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 89dd6e64-55d2-37bb-ade3-8db271764e3e | -3.65303 | -55.46416 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ddf04a0-3959-3fb6-a67f-62aad68af112 | -3.61502 | -55.47213 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02343e52-b643-35ee-b4e4-2e8449f714b6 | -11.32466 | -46.68763 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 681fcaaf-2d4e-3efb-b384-dd6351faeeb6 | -2.48306 | -56.12212 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fab11a62-e4f5-3dbc-ade8-9ce96264a99c | -2.50327 | -56.15779 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 35f25032-1fe0-36b7-8b1e-37d030a10e87 | -2.48953 | -56.16342 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9260790f-3246-39aa-bb10-f9eea5c0c131 | -5.48696 | -41.39763 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5d0a6b9c-6dcb-3534-9382-602c94997de3 | -7.48526 | -42.79755 | 2026-10-08 04:46:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3358237e-e51a-38a0-92a1-e18fe95a86f4 | -4.23843 | -49.98861 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d1a312d-8281-3953-8230-02732c00db84 | -4.93658 | -55.81659 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a76c472-f2a9-3f82-a7eb-de8981f9d068 | -3.96311 | -56.12679 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 951414ab-23e2-3191-9ccf-e2cf0717e86a | -3.56278 | -54.48321 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e92ef00d-2815-3c41-a986-ed22f0bd1cf1 | -3.73132 | -58.86294 | 2026-10-08 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 789d1c6d-d69e-3997-8ef6-ff075ede9d22 | -3.02417 | -53.86809 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55950027-d65c-3028-ad14-305c7010386d | -3.28634 | -54.01183 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5cba97ef-8ce1-3c4a-8c63-53afe0f94441 | -10.42714 | -49.25119 | 2026-10-08 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README84.md)
