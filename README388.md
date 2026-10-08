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

## Dados Diários - Página 388

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5eb7dd24-5f9b-3640-8fa0-09e6a2534768 | -5.4806 | -44.6029 | 2026-10-08 18:10:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 14cafb97-a47e-3045-a7c7-da193560850b | -1.5123 | -54.5361 | 2026-10-08 18:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c52a2dea-3e1b-3c4e-86b3-6c4d11465492 | -12.2123 | -44.7457 | 2026-10-08 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 53de418c-0988-35b0-8ae1-79afb107c93e | -11.6181 | -43.6669 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| c03f91fe-8616-3118-b97e-a5acc89211fd | -2.9707 | -57.7585 | 2026-10-08 18:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 29e2099e-122c-3a5a-bab2-12e56ef4b275 | -3.0374 | -53.9268 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 4c0d3c44-3603-345a-8bf9-9c68dfe6cf3d | -1.5123 | -54.5161 | 2026-10-08 18:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 869aefaf-0168-3916-a608-bd1e0e89eb25 | -11.755 | -43.5275 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.4 |
| f11f04fc-e6ae-39d5-a576-4017d8bcbdc3 | -6.1977 | -52.7886 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| e0167df6-11ee-395a-b665-272346bd1677 | -2.4989 | -56.1069 | 2026-10-08 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| a46061e0-38e4-3f0f-b961-02103b5e8495 | -2.4942 | -58.0768 | 2026-10-08 18:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 5cfb4e1e-918f-34a7-b27b-443f25031d3f | -8.0766 | -45.6112 | 2026-10-08 18:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| e5ce667c-d1ac-3322-beb5-4738a6be0264 | -13.1641 | -54.3178 | 2026-10-08 18:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 366.5 |
| 05b1f980-e05b-3864-8194-2d474d1eeb00 | -6.737 | -55.0674 | 2026-10-08 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 39fb53fe-7b98-3257-8cf4-ea34db5108a9 | -11.7738 | -43.5482 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 279.2 |
| 638d812b-2b0d-311a-97a2-7f344f7d54cd | -8.5313 | -46.911 | 2026-10-08 18:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| f8917c68-cd74-362f-8496-ff38784669e1 | -3.6603 | -54.512 | 2026-10-08 18:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 84addff3-1308-30ae-b2df-7bb7412a42a6 | -2.8434 | -57.4696 | 2026-10-08 18:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 2ae03575-5bf2-30a0-b2b3-bdd62da6b820 | -3.2633 | -57.8883 | 2026-10-08 18:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 180.0 |
| 924d0724-5f10-3448-a1a9-8270e4f33ea8 | -14.3608 | -55.032 | 2026-10-08 18:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 39bef76c-7b8e-3f25-8019-d4eff31bdfb1 | -3.1114 | -53.7839 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| eaab3364-809d-3544-96c0-eb753fddf7f6 | -11.7935 | -43.5215 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 70be8550-2a60-323e-8e69-698f3ead6fee | -5.1333 | -46.0253 | 2026-10-08 18:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 6b0795f1-9a9d-3154-96d3-362d54c70b5b | -12.1549 | -44.7314 | 2026-10-08 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 250.2 |
| e069d08e-76cf-39f0-918d-21105ae33718 | -9.5003 | -66.8017 | 2026-10-08 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 6c55b6b0-6497-353d-97b0-ad23d214d968 | -3.0447 | -57.4851 | 2026-10-08 18:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 857ac191-f873-3be8-b3a0-7be29621bbc9 | -11.2657 | -45.209 | 2026-10-08 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| c30f704d-5eb7-3da8-9f5b-d9331d74a1db | -10.7936 | -47.328 | 2026-10-08 18:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 8c13199e-3c94-3808-816d-847664c2a012 | -7.5354 | -42.088 | 2026-10-08 18:10:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| ce66cd7b-cd06-3e27-acc7-1da5e3b11efa | 1.6937 | -55.6263 | 2026-10-08 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 53929811-1b2f-39b1-8792-5031762a13f4 | -15.0346 | -42.4941 | 2026-10-08 18:10:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 88.6 |
| c9950cc1-5f1f-35c6-a551-a27895427b8f | -6.1484 | -51.927 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 185.4 |
| cd742329-cf0b-3e6a-87a2-c79340f8608b | -7.4694 | -42.8551 | 2026-10-08 18:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 144.9 |
| 1254f395-0746-32ba-8b97-0fde1c16f0f4 | -1.801 | -57.1161 | 2026-10-08 18:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 9cddfdf1-885e-3864-844b-5e28f1cc4635 | -5.9647 | -40.9383 | 2026-10-08 18:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 1d024df4-8e8e-359b-9d5d-5434d3f92850 | -3.4095 | -58.0013 | 2026-10-08 18:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 9dd8b86f-43bb-3982-8872-5b171a226268 | -9.1256 | -67.8507 | 2026-10-08 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 3ecef2c7-32da-31b2-a2d5-ffb0552ab6b1 | -3.5234 | -44.3267 | 2026-10-08 18:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 9b4dfe11-28dc-324b-97b2-479bf86cbec7 | -2.572 | -56.1842 | 2026-10-08 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 383.6 |
| 9552d7b0-e7bd-32e9-9c91-e6bddcf83ed7 | 1.7304 | -55.5863 | 2026-10-08 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 10fb1347-780d-30fb-9bc0-ff5d1910f490 | -5.4142 | -45.8734 | 2026-10-08 18:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 6a9441b3-141a-366f-b74f-49a4610b3b7a | -11.6369 | -43.6876 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 287.0 |
| f996630b-8588-322e-b74f-2fa4915d01e5 | -11.1354 | -46.1623 | 2026-10-08 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 1d629fcb-ad22-3158-91c5-ecff55f6f734 | -9.9018 | -44.7917 | 2026-10-08 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 637af01d-6cf1-34bb-abfd-fd64c376844f | -10.9384 | -45.3916 | 2026-10-08 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 20b1a071-86d6-3d51-9159-76e32d34abed | -12.0256 | -43.4371 | 2026-10-08 18:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 535.9 |
| de25b38e-eda0-3b92-ba3e-58cc80702712 | -9.1072 | -67.8141 | 2026-10-08 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 416baa38-f94f-37b4-ac56-3d8a35fc8062 | -6.6027 | -37.8944 | 2026-10-08 18:10:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 172.0 |
| 1eeb02e9-5d79-3695-ae0e-a7bd3ca6ad2e | -6.4567 | -55.4809 | 2026-10-08 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| cda42a72-a752-3066-b385-3fac0c81d91e | -3.0008 | -53.8874 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 850e0e8e-b83a-3f71-91b9-6915979a3a25 | -5.3718 | -44.1981 | 2026-10-08 18:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| d1218c50-6fa7-3f42-a99c-ccff7e64c884 | -6.9328 | -43.6799 | 2026-10-08 18:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 20ed88c1-d340-3afc-b068-4385df8f6cea | -4.1025 | -44.1149 | 2026-10-08 18:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 156.9 |
| c082fb82-b2bd-3656-88b2-e55f4bd0c767 | -2.9819 | -54.0488 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 180.5 |
| e814fcb8-6b94-3f4d-83c5-ec55138a0481 | -12.2316 | -44.7427 | 2026-10-08 18:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 222.8 |
| bc725fd1-ab6b-39f7-b534-6c78c014a8ba | -11.6382 | -43.6166 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| fea649d6-c919-31c5-acc2-ec9b265fd689 | -9.9589 | -43.5516 | 2026-10-08 18:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| daf10a31-b9bf-322b-8937-98cc5c6966f9 | 3.5448 | -51.2772 | 2026-10-08 18:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 807e9233-2a7b-3d7e-9498-f002caf4681f | -11.6387 | -43.5929 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 260.8 |
| 2d69075e-30d8-3c66-94c6-b397d69d7d1e | -3.8756 | -55.8184 | 2026-10-08 18:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| af74d51d-0477-3e39-8466-1b4dedb073c5 | -3.3911 | -58.0405 | 2026-10-08 18:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d5da500e-a7c4-362e-ab14-52443053452d | -9.4818 | -66.8022 | 2026-10-08 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 36862989-0319-3fc5-a23a-46bcb3aa98db | -7.1442 | -55.1257 | 2026-10-08 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| e9134aba-4381-3de3-b549-da53756c92fd | -12.2311 | -44.7661 | 2026-10-08 18:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 560.7 |
| 58ab299b-bfe6-393f-93bc-c28bfce3e65a | -2.0447 | -54.3085 | 2026-10-08 18:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 50d8b84a-68e7-300f-9d74-3532c76da2b6 | -6.2127 | -53.2779 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 1c01a398-6a33-3d34-aaf2-719c3fe701d6 | -3.0925 | -53.9455 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 471.7 |
| 4d76b63f-84fc-390f-a74c-2c1639bf4e39 | -2.8346 | -54.1326 | 2026-10-08 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 188.0 |
| 5ec9ec8d-9047-34cf-92d6-c82c9c941b51 | -6.2162 | -52.7876 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| cd658da9-9eeb-3d49-ba94-44d2e118555d | -3.2268 | -57.8696 | 2026-10-08 18:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| cb83c361-6ad1-3e9a-ac7e-16fa62f2ee8e | -3.3912 | -58.0017 | 2026-10-08 18:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 3116331f-6ac1-3fc6-9706-7aaf739666cd | -6.7185 | -55.0684 | 2026-10-08 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| fd6eab4f-34ab-3fb2-8028-5542fc56573e | -6.8762 | -43.7083 | 2026-10-08 18:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 1a88bd73-dbfc-3020-96da-1803d584139d | 2.0047 | -55.8786 | 2026-10-08 18:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 1fe4e4ee-a6d2-3fef-bbab-6a12adf7f439 | -9.8817 | -44.8632 | 2026-10-08 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 6e77589a-0e1b-3b21-8873-07efa29ba8da | -6.0075 | -53.5122 | 2026-10-08 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| edc3f64c-8c38-3c32-9052-7ca4eca7be2d | -3.2957 | -49.1202 | 2026-10-08 18:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 121530bc-f7d4-34b3-a540-a1e7a3b0ec15 | -3.1506 | -58.9134 | 2026-10-08 18:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| cc16332f-1e48-3061-93ea-8598c0db6fbc | -2.9265 | -54.1305 | 2026-10-08 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 8e3137fe-7848-3124-b0bf-cba33f6f2769 | -2.9082 | -54.1108 | 2026-10-08 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| f97a7655-2f04-31ce-88b3-656e5687815a | -6.1496 | -51.7614 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| e4797207-c93f-3def-9faf-22f8fba65746 | -12.0448 | -43.434 | 2026-10-08 18:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 12bb6669-2bc7-328e-9cd6-93a0a6c7c972 | -5.9835 | -40.9367 | 2026-10-08 18:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 176.4 |
| dd73d017-aa2c-3c8e-b175-7991ba2aac44 | -6.1603 | -52.8315 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| a32649bd-5885-3449-946b-33f277d9c40a | -13.3671 | -43.8742 | 2026-10-08 18:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 718cb859-726c-3830-9b7e-9c9f54545461 | -9.2745 | -67.6433 | 2026-10-08 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 72380acc-25ee-31bb-bcda-05cab0300ca9 | -2.5492 | -58.0373 | 2026-10-08 18:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 171.3 |
| f65120c5-22cd-3c59-89c0-47f9ed051855 | -11.619 | -43.6196 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 366.3 |
| 2ca6f108-09e9-3373-ab37-5048557f48fb | -4.5733 | -55.9943 | 2026-10-08 18:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 2e9af4fd-d163-3402-9bcc-ec3b9393ce14 | -11.8696 | -43.5568 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| b7a53d80-5c61-3237-8b05-8366aef37f59 | -2.7152 | -57.472 | 2026-10-08 18:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0c963ef4-e507-31e5-afd6-a0db0db60597 | -6.2157 | -52.8695 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 5d1c05a7-b071-3d7f-9ee2-72784473e7b8 | -6.1429 | -47.9432 | 2026-10-08 18:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 155.9 |
| fd3367d2-3dbe-3428-8b06-0bbb6ac1bda4 | -2.5903 | -56.1642 | 2026-10-08 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 246.1 |
| 205d6774-b2f6-3a87-898e-c5305eda093c | -3.188 | -58.6241 | 2026-10-08 18:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 9f90350f-b43d-3b81-9709-94c18ac0079a | -9.1253 | -67.9432 | 2026-10-08 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 124c8358-68c5-3152-9237-8ba3193bcd21 | -7.4886 | -42.8295 | 2026-10-08 18:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| c384803d-8b70-39b9-98eb-ebd79ab71490 | -5.3905 | -44.1968 | 2026-10-08 18:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| fc9bd7d3-f37c-35dc-9077-243f8959fa8b | -14.0667 | -43.8185 | 2026-10-08 18:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 243.8 |
| 3f557ec9-28d6-3269-9c66-f98f240434c2 | -3.2761 | -54.0011 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |


[Clique aqui para ver as próximas entradas](README389.md)
