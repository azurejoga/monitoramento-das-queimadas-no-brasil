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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec35c411-8641-3c56-a7e2-a968eab04faf | -7.55119 | -47.36089 | 2025-10-24 03:47:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e361348a-ec5d-3615-b9bc-fcc9abd6aa04 | -8.43474 | -45.59161 | 2025-10-24 03:47:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9af71d11-d31b-3805-a905-7c2cacc51c4a | -6.61583 | -42.10256 | 2025-10-24 03:47:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a52ca782-5a7f-312d-bf6e-66fa4dcb16c1 | -8.34547 | -46.17939 | 2025-10-24 03:47:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75b2a5d5-b4a6-3bc4-a5af-fae85e82bd8f | -8.61795 | -44.80995 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dff3a6f9-ee3d-30c6-ab14-4ee28e49d99d | -8.05839 | -46.48158 | 2025-10-24 03:47:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd334c1a-d7be-3959-9fd4-aefc30903b23 | -7.27803 | -50.00698 | 2025-10-24 03:47:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfa04b86-1f5d-355e-b766-b35fc8c2dc6b | -7.20865 | -39.08394 | 2025-10-24 03:47:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 18b67e19-a4b5-3a0a-be77-82e07c2803cc | -6.42925 | -45.67253 | 2025-10-24 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5400156e-d5bb-3cf3-b6e4-22d6a579e776 | -6.53865 | -41.68581 | 2025-10-24 03:47:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 94e7cbe2-c9a0-3cff-b3c3-50ed57b943f4 | -8.19077 | -44.43699 | 2025-10-24 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| df69b2b5-e9b3-30ac-ab81-873f293b2050 | -1.10532 | -48.88613 | 2025-10-24 03:47:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 824d44df-f5dc-3246-9de8-ba3e70abff56 | -6.30596 | -41.88266 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1fceeded-34b3-38a1-b35a-2f89075ac889 | -7.97934 | -47.23924 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fce4429f-5fb6-3095-a28d-2a75b4796974 | -7.64136 | -42.29883 | 2025-10-24 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c50dabf8-c578-3c62-9b39-f22b2a999342 | -14.52145 | -47.95153 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 128ffe4a-16bf-3169-9120-1a7fab769bd3 | -2.81433 | -49.14259 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 615841f3-98e3-3213-8456-99046770491f | -13.53637 | -47.54599 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06fdec94-0306-37ed-93ed-bc855d8d30b3 | -4.28692 | -40.70308 | 2025-10-24 03:49:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3b53d165-abb6-3182-b00d-6324aaeb5de6 | -9.59802 | -46.90466 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b19e9d34-030b-38a5-957b-12a1ad728d51 | -12.82145 | -48.63315 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58440b67-dc70-3b95-a87e-0af1df134700 | -15.6287 | -48.54742 | 2025-10-24 03:49:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 464021df-990b-30e0-a662-5fc8d14d5929 | -9.60683 | -46.91729 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dbe5b19a-b723-36c8-81b1-43b1489b9f58 | -11.97943 | -49.17786 | 2025-10-24 03:49:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42ea9bf8-1272-3875-88ae-3e727ee2a30d | -10.95999 | -45.08135 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2700915-f772-350a-946a-40dcaa75ab1d | -5.58724 | -41.32212 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d64e30e2-d6bd-3ec3-8206-e859f548416b | -9.26803 | -46.46405 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f8ada67-44f4-39e7-a797-f9171a014822 | -14.9245 | -48.1395 | 2025-10-24 03:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5dc15461-8318-3285-8c88-46d1c3597769 | -13.91557 | -48.38825 | 2025-10-24 03:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d1a6ac6-013c-3f8d-82c1-62f3e0b5634b | -14.43061 | -50.9575 | 2025-10-24 03:49:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a7d61510-f680-3799-8d3e-ccda0525033e | -12.29612 | -45.52638 | 2025-10-24 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ca34b19b-fade-37cf-8970-8015a191bbfd | -10.04677 | -47.09968 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a53c09d2-e269-3662-bdd8-5905cda27a78 | -14.43174 | -50.95218 | 2025-10-24 03:49:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d740463f-4481-3f6d-ab09-b5fd69c1421d | -12.02373 | -46.91992 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9ab6df1-265d-3ace-95e7-8217938de4fc | -15.49653 | -45.98531 | 2025-10-24 03:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c16e0035-6532-35c7-b3d6-7cd3a886714e | -9.64423 | -46.89563 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12a80a2c-0fc5-39f5-aae7-09899c84e833 | -12.81231 | -50.9496 | 2025-10-24 03:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 170d5b20-94f4-3acc-8048-955fbf6e8378 | -9.60617 | -46.92085 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 43177b1b-4d14-3b90-be62-e089ba17472e | -4.00039 | -43.2812 | 2025-10-24 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8968723e-126d-3d95-8344-875047881e81 | -15.95074 | -49.60505 | 2025-10-24 03:49:00 | NOAA-21 | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff5f3538-f21a-340e-8810-9c27cf575a84 | -10.02478 | -47.08797 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abf33639-1da4-3f4d-be6f-103b1022fcaf | -11.35916 | -45.95971 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 53a475e7-4184-3a74-aa9c-b392d14f60c8 | -14.53914 | -48.02975 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d592622-2f4c-3413-98ab-d6c8a4688824 | -10.04607 | -47.10332 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5e30930-8cfb-3939-89cd-4a9c962cee92 | -15.8366 | -49.09341 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b2fada2-59a8-32d2-a465-7e5af3c2bf8a | -13.15592 | -47.09708 | 2025-10-24 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6da4ea40-f9ea-38b3-bb6a-b7060109464a | -10.88739 | -46.04763 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16690dd0-d58f-39b8-ae60-e1049d1e85c3 | -10.94916 | -50.38097 | 2025-10-24 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b26cebc1-7fe0-35d1-8f77-578d804dfe11 | -9.55502 | -46.70075 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a98cc141-4bef-3d7f-95e0-73c9a7531dcb | -12.06999 | -46.44225 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c2daaeb4-c853-327c-8877-61f04b67e2df | -11.09686 | -41.61665 | 2025-10-24 03:49:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 09b6d14f-c314-398e-8ee4-049112028ac2 | -16.47799 | -46.47448 | 2025-10-24 03:49:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f96afb6-0e14-3032-9acf-345f08b479d9 | -12.81893 | -47.24051 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de864c93-3caf-3905-b523-d1c1687671ad | -12.31515 | -47.26468 | 2025-10-24 03:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d0de1652-8387-36d9-b95f-493ffc727c16 | -13.08937 | -47.55682 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfb8d9e3-3433-32c3-889d-ce8bead0dc60 | -3.99923 | -43.2796 | 2025-10-24 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4413d0e-4543-3816-9ca6-acfe19f90058 | -12.07621 | -46.40921 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b78aa8d-99fd-3eec-af7f-caceacb4e572 | -13.53668 | -47.54475 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a8511fb-a1ac-346b-9161-b25aad4f0cd9 | -13.34705 | -47.97565 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8588e17-b869-383a-ab4c-4a10ddcaddd0 | -9.26094 | -46.47308 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bff581a3-2f3b-343f-93fd-72e07038428e | -12.05902 | -46.41807 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df778857-8b70-364b-9190-4916d075a817 | -6.00728 | -40.22341 | 2025-10-24 03:49:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d69e9ad-1861-380d-a4e3-3d2ad0a8ff78 | -11.29115 | -45.36965 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d65f6b5-78a1-3dd1-95b9-379d6b248d6b | -14.47796 | -47.92181 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e700a8f0-00fc-31a7-9cf2-24cd05296696 | -13.28202 | -47.4856 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58071a72-bf86-3c2b-a473-b445868740b6 | -12.72406 | -46.94532 | 2025-10-24 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68f7e8f2-d664-3d4f-8345-5ab6de1ac08f | -15.94389 | -45.21648 | 2025-10-24 03:49:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 735436a3-b93b-3e3f-943a-b9c842efecf3 | -5.43668 | -36.81757 | 2025-10-24 03:49:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 08390c29-1120-30c2-aecd-5a9f06cc2da4 | -3.029 | -49.49414 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 64f3dea3-d76c-3e64-922e-bf1449860547 | -9.96783 | -46.34445 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a8f56ed-0f91-33b5-b107-e929fec03a27 | -2.81404 | -49.14377 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 32e2131b-3694-37ea-8606-b5a9c140cb39 | -4.05866 | -46.74814 | 2025-10-24 03:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49ec8587-f587-3e41-8771-90a64dd0df65 | -9.60749 | -46.9137 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3e47c67a-0e97-323d-8b0b-51b4835f28a0 | -5.54637 | -41.37191 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 02176653-3055-3970-aee2-2b2da12c40c5 | -14.7476 | -46.60368 | 2025-10-24 03:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3306dfc-6fcd-3ef1-ab0f-ea64194fefa3 | -13.34542 | -47.97488 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38b4b3f5-5698-3fd8-a560-5d5ce78c0ee8 | -9.96837 | -46.34159 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d745f05b-e8a4-3883-9157-7ac15a49142c | -12.0601 | -46.41235 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4664179e-55d2-302f-8119-52e20851d7d6 | -8.83617 | -48.85749 | 2025-10-24 03:49:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38317500-43aa-31eb-858e-0371ee0c7f9a | -15.21069 | -47.95722 | 2025-10-24 03:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 590c85a1-8d99-30c8-a739-033027349511 | -9.60141 | -46.91643 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 2804a456-b6ab-39ba-a76d-950bb19a0dc1 | -12.07507 | -46.41529 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52850502-8956-3463-b5cf-7e41575b2356 | -13.24845 | -47.88616 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5481207-147d-3eab-ae5d-9c0b022d6970 | -5.8205 | -40.80191 | 2025-10-24 03:49:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0a1607cb-03cb-329a-825b-0426e01a8eb5 | -4.2792 | -40.70146 | 2025-10-24 03:49:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 67a1bfb8-b2c1-3091-91f7-7dc548d117e0 | -10.89074 | -48.04838 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6ca134a0-cddc-30a2-88bb-9112dd445230 | -13.76224 | -48.3553 | 2025-10-24 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 774035e9-56cb-32db-be3d-aa26c2a085b5 | -13.88526 | -48.36926 | 2025-10-24 03:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c5c4d55-a887-32fb-a2db-cc8ee7df1291 | -5.38212 | -41.55519 | 2025-10-24 03:49:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 15ea65d5-5fa1-32da-979d-48800e51fc69 | -9.2704 | -46.45101 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f91c356-42a6-3718-ab87-403b9b8f276f | -10.56195 | -50.00005 | 2025-10-24 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fc833d6b-b837-33cb-9473-a3c6768ce320 | -14.77188 | -49.29406 | 2025-10-24 03:49:00 | NOAA-21 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 375ff466-2e07-38e5-ad39-9c8211b8fa9e | -5.43378 | -40.88337 | 2025-10-24 03:49:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5a232798-85f3-33a8-a95d-1f0ed89e7abb | -3.71319 | -44.41456 | 2025-10-24 03:49:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 010f48f3-f3ad-3bae-8ac8-a54caf6b0759 | -14.26903 | -48.07485 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e48316c0-bd2a-3460-b7b8-0e23f2cce74e | -12.3725 | -51.47344 | 2025-10-24 03:49:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f8b85184-af76-34f5-86db-236794fa79b0 | -9.26214 | -46.46653 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7464fa9-d0c2-3479-ac42-e59c4b821259 | -13.35817 | -47.96693 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3e65622-919b-3c8e-ac1b-f58631b1a199 | -13.92093 | -50.26418 | 2025-10-24 03:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 067aa7c7-68ac-3aee-9fc4-54b0a828647a | -9.23063 | -45.61562 | 2025-10-24 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README7.md)
