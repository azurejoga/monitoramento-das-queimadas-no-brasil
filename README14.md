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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fbdc45e-56ae-34ba-8539-83f026e2e194 | -5.35222 | -44.79688 | 2025-09-09 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2da78ea2-6512-391d-9a09-6f78a5ab9a8c | -10.27514 | -48.81807 | 2025-09-09 03:42:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6275be89-4b6b-3015-8246-7fc11dc773b4 | -5.68549 | -43.90485 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2b51991-664b-3756-8411-d853079cc855 | -8.20878 | -44.76976 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 346fe626-7444-33fb-a935-364b135ec7e5 | -6.42829 | -44.06736 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7667cf63-1c20-300a-889e-6df33dad71de | -10.97003 | -45.11878 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| d48d1304-394e-3213-8f81-efb93d7d2fe7 | -10.80493 | -48.28912 | 2025-09-09 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e647e1c2-32aa-3f0d-90b6-b69d94a6f8f1 | -10.9655 | -45.1199 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c79e6294-7ee7-3c6a-a899-ef7ffe919edd | -5.72275 | -45.40668 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69eb6553-9ab1-3b80-acd7-ae46eb162548 | -5.87831 | -43.97419 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8669b1a-9fa3-3a34-af01-cfa7e729950a | -7.80085 | -45.21198 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b321e01-d187-378e-8c77-67b4da9bd30f | -11.43875 | -43.64717 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c0b744f2-1a7c-31f0-a48a-0dce834dba27 | -10.95531 | -46.80943 | 2025-09-09 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0c782c5-89cf-31f5-907b-23619829822b | -6.1788 | -43.38284 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5f11bf1-2054-34f5-b1f3-1e0ec5b911a6 | -10.97309 | -45.10819 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f766ca0f-a4ea-3281-832d-bc5626820297 | -6.80535 | -43.56654 | 2025-09-09 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0c7848c-0ccd-3ea2-b920-4087f156a77e | -9.15348 | -45.57676 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc767046-1fa9-3706-a4ac-560f2bf0a086 | -9.14852 | -45.57121 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cab65817-dceb-3e18-bce0-5f040f7a527b | -11.41987 | -43.59241 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5e42973-f65e-3aa9-928f-9ed0c6219c79 | -10.97236 | -45.10601 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| a41c0da1-85b3-37db-aaaf-358ee0ba9eaf | -7.43174 | -45.21402 | 2025-09-09 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5632a380-a2cb-360d-95be-d082c1fb608c | -8.05013 | -48.65427 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 782fd6ba-f4a0-381a-bb2a-a3719438aebe | -6.61878 | -44.00022 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94771655-f831-33d9-90e3-1a34c51d8c32 | -5.81355 | -43.97367 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6b5f3556-ed4a-30cc-8103-39cab0a43ea0 | -7.70871 | -44.75269 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6b3bdc2-dc88-3c76-b8c8-0c08fcc8faa9 | -6.20814 | -43.3621 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d2f6c7b-47d4-33ef-82cf-b1356670a1d2 | -11.17626 | -46.12298 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1cf6fc6-1e60-3103-9f4e-559394881c01 | -11.14738 | -45.2718 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8589d3da-f908-38a4-8216-fa4457de81a0 | -10.97118 | -45.1125 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 550ca726-5395-39ec-b03b-7b88a8e11b0c | -7.13994 | -46.05988 | 2025-09-09 03:42:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60422f79-1417-3bbb-9321-5624fdaad89a | -10.97007 | -45.12399 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dfe7183b-40f2-3b43-88d6-99464472efc3 | -5.67498 | -43.90165 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63b7c05c-fef0-3756-b0d4-e830c7f012b1 | -11.03068 | -45.93343 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35c7a811-9466-3196-808a-37164ae2086c | -6.48184 | -38.82863 | 2025-09-09 03:42:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 68e91c2e-841c-3389-834e-ebb681557b31 | -9.50413 | -48.27678 | 2025-09-09 03:42:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e184e06-043b-34f7-88e8-338770a9dd71 | -11.3788 | -45.59451 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d83f9da-494c-3f8c-ad14-0e7aaf8da985 | -8.20714 | -44.76958 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f7a0495-258c-3248-9798-ff412e7126fa | -6.09805 | -44.13549 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6286958c-e368-39be-9d0e-f9d4ce83a7e5 | -10.97827 | -45.10911 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 0b01f3eb-ce77-34df-a4b3-e9bd916a2533 | -10.96543 | -45.11467 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 81556eb9-3ae1-3300-8f50-5b28cd7274cb | -10.74431 | -48.18618 | 2025-09-09 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1bc72560-3ffb-38db-87fd-a7447eeded7e | -10.73929 | -46.33331 | 2025-09-09 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3477f896-c0e8-3af5-b473-822c0ed9a356 | -7.57004 | -44.66027 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f53086f-38ff-3ec1-8be9-ee2defdf3fd6 | -8.33899 | -45.06168 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55c71749-e5bb-358d-b25c-02f42c0d6d30 | -7.72737 | -44.74096 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acd1c10f-f96b-3538-96aa-e4a839c92f14 | -9.85366 | -47.79356 | 2025-09-09 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd19811e-4e4b-3272-a2fc-f7f0bba3fa7b | -6.40336 | -44.48804 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27e66237-55a0-30de-9ba1-3fef6937c191 | -7.8008 | -45.21249 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e941f746-c9a6-3d04-b407-f040dd1416d6 | -6.38773 | -44.45109 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac4849fd-d67e-3008-9eea-f48050445afe | -8.03435 | -48.62742 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 025966f9-a07a-3557-a0d5-96cfd6ab0c75 | -5.57607 | -45.04626 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| b2e54cb0-da67-3342-97ae-0487e8e3b780 | -11.38257 | -43.53496 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3953a21a-7bcf-31e5-9239-25a3450a5f66 | -7.70942 | -44.74877 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84195996-57c5-3f6f-8deb-1d073b31a918 | -6.18231 | -43.39246 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35b97106-1ad6-345a-bc27-f6303fb33346 | -7.1458 | -46.061 | 2025-09-09 03:42:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac2f70f0-bfcd-3820-9276-cfd449cb475d | -5.66582 | -45.45967 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 962a32f7-e493-3775-b853-e4b0e00b349d | -11.42361 | -43.59818 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a9ff8f5e-f4d0-3775-8748-ed812c3c5cae | -5.67162 | -45.46064 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5c43127-0bec-39ac-b372-d65b9ff9f6f3 | -8.20171 | -44.82838 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 953330d7-97e8-3371-b3e2-75847cf139d4 | -6.67579 | -44.55797 | 2025-09-09 03:42:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09bb9b0d-2714-32f0-871d-4febf0f389c3 | -5.68027 | -43.90395 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8084cc5b-2792-399f-8632-29312c7cdf72 | -11.42824 | -43.59906 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3b9f0e6-3a9a-3ab9-9894-9ae0ffcb9618 | -5.94806 | -44.16511 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37b89158-98ba-3ccf-b0b8-aee0f868721c | -5.85449 | -43.86174 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5caa9bb3-9281-33cd-af89-f9382f1934b5 | -5.54392 | -45.16483 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| af4cb77e-f586-3f46-b0ba-df1f9c30acb3 | -8.21848 | -44.76751 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39d9d478-29ea-3c95-b4e6-73b41bf72174 | -8.37367 | -45.02363 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13fe6215-23ab-3931-9059-6ae793fe4ded | -8.39816 | -49.10046 | 2025-09-09 03:42:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e0fa727-fd4e-39ed-a738-96e11104616c | -9.7426 | -43.51957 | 2025-09-09 03:42:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8d711aa-3e03-3860-bf58-84537beb21a3 | -6.5626 | -43.15092 | 2025-09-09 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f390e8b0-db01-31db-8d23-b5f5285838e8 | -8.04273 | -48.64613 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0425943-4055-3051-baad-dd9826844080 | -5.81658 | -45.65133 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8c84f63-42d4-3f6a-b1c1-2a85ca022483 | -11.18175 | -46.12409 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b00a9a5-4a4b-375c-a8c1-b395a1616da0 | -7.55774 | -44.66762 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1a6d90a-9f74-3ac4-9b88-cd28cb761ffb | -10.98467 | -45.10361 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| a1ee950a-0573-36c8-88cd-e7a967b79a5d | -10.1494 | -46.19841 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ceff476-05b4-30a2-99e6-2ac6899ea82a | -6.20388 | -41.02228 | 2025-09-09 03:42:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10d03f13-6057-3151-8e72-c56c817d55aa | -10.98405 | -45.10683 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 7f9005d0-c08d-34c1-bb78-d329fabbc8de | -6.06418 | -43.12485 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f1cf408c-b15d-374d-a8bc-7fea5f110d6d | -6.34691 | -43.78473 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 368b5b4f-7e85-3699-90a0-954aaea5b178 | -6.20569 | -45.03568 | 2025-09-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0177f16a-af83-38ab-bda0-537baa136d83 | -5.57539 | -45.05021 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 4479de15-526c-373d-8ddf-a78b9cd8c53c | -7.79704 | -46.09619 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b41a1006-170a-3081-873d-132d5af61bbc | -10.7718 | -47.72693 | 2025-09-09 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7200f49-81df-33bd-9b69-b6e8a7f1ffb6 | -10.33216 | -47.73751 | 2025-09-09 03:42:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 632a702d-af22-314b-857d-59e47a8a42fc | -6.29368 | -43.81746 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61265e6c-6a1c-3e7e-9d74-47728da35fc6 | -10.73365 | -46.33232 | 2025-09-09 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39edc390-6229-3bbf-9c71-f94a7effbb3e | -5.68083 | -43.90075 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16264549-2519-3075-a959-ecb9a86f3a81 | -8.05813 | -48.63874 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9b2fd780-5789-3228-9cab-a59391a94429 | -6.40877 | -44.48872 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad16de70-00fb-316e-9f98-73fb8366ca4b | -9.7219 | -46.80495 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 673b70b9-bb0e-3b43-b5a6-b9d09954520a | -5.99407 | -46.20259 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b53960e7-9088-39c1-8891-27ffc9d1cf45 | -6.48256 | -38.82427 | 2025-09-09 03:42:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d2802112-0d94-3dc5-98e0-2f993b94b78d | -8.23316 | -49.54249 | 2025-09-09 03:42:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbd4f724-7f80-3df6-8f27-e410efcadab8 | -5.81555 | -44.11825 | 2025-09-09 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20daab4b-5a51-3ba2-99f8-ce9ad9b4b16a | -5.6872 | -43.89516 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22d8477f-43c2-3d02-b5ce-f50ab532ad1d | -5.70342 | -43.89471 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f70ca143-b97a-3012-b51a-1e3da1d40d9a | -6.0632 | -43.13045 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3e5a7677-2593-356c-b614-dedca517411e | -7.02611 | -44.94688 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd33d533-2975-38cf-859c-38a6dac64dc2 | -7.47388 | -34.91697 | 2025-09-09 03:42:00 | NOAA-20 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README15.md)
