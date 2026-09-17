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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3d98c8c-0aea-3581-8f06-7bdc778d0537 | -9.8322 | -48.3417 | 2026-09-17 17:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| e1e8a7f8-01ee-3882-a844-a83b1d6a52fb | -9.3569 | -50.1583 | 2026-09-17 17:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 4de41eef-0c0a-3359-8496-1dec7ab65ce9 | -9.3567 | -50.1796 | 2026-09-17 17:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 373803f9-de2e-3ac4-8a30-16fbf5a64393 | -9.3758 | -50.1565 | 2026-09-17 17:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 7790135e-4b43-39f4-ac5e-848d3e3252f2 | -9.5512 | -45.4296 | 2026-09-17 17:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 5b7fd00b-a715-322c-9a6b-4a35bd412b65 | -7.8221 | -44.8632 | 2026-09-17 17:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 457.6 |
| 026b5f78-7d0f-36a6-bcf0-bc0a124b76b0 | -6.7463 | -59.4416 | 2026-09-17 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 0096940b-01a8-36a5-b06e-c80d779b47ee | -10.1168 | -45.6346 | 2026-09-17 17:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 206.9 |
| 8b55cdcc-48cb-31ef-827a-1e56b04eca53 | -10.7923 | -46.1845 | 2026-09-17 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 1585de30-07b6-3fa5-80a5-1d1e28f1cdb9 | -7.8036 | -44.8422 | 2026-09-17 17:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 588.2 |
| 3b554653-d59a-3f91-92e5-2ca4fea0e2c1 | -12.6826 | -54.6763 | 2026-09-17 17:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 143.3 |
| acf5c33f-10e4-3bd7-9609-82c0ee3e41c4 | -9.7497 | -46.1089 | 2026-09-17 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 6a94b7c5-303c-38f0-8ba8-c1f20992b931 | -6.7816 | -59.7288 | 2026-09-17 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| b169e1e9-0fc3-3ec5-8040-32356375e81a | -9.7877 | -46.1045 | 2026-09-17 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 126bb007-bb14-3d13-8683-133d94b6fa4e | -9.8322 | -48.3417 | 2026-09-17 17:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 6cee5383-b8d5-3599-b88b-2b74b955b352 | -7.1384 | -42.1529 | 2026-09-17 17:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 115.5 |
| 1eb74cf1-565a-367a-afe2-b2d8d079f165 | -9.4137 | -50.1317 | 2026-09-17 17:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 8d0c8720-212f-370d-983e-59b089cf257d | -8.58 | -44.5552 | 2026-09-17 17:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 236.8 |
| c969083f-9b6a-3f30-a9da-55925e5d5c49 | -10.8308 | -46.1569 | 2026-09-17 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 83f9bd40-0035-34ce-bf4d-b126039dabf6 | -6.1478 | -57.6825 | 2026-09-17 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| ad310c90-e8e4-31b4-a452-710d55597ae4 | -9.3755 | -50.1779 | 2026-09-17 17:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 8b4ac9c8-6823-38f4-8a22-83f2e356eea1 | -7.8224 | -44.8404 | 2026-09-17 17:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 338.8 |
| 4d3c1e69-698e-3518-9749-ac8c2ac1f5b3 | -7.8033 | -44.8651 | 2026-09-17 17:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 358.9 |
| e345bd84-33aa-3b76-b5dd-b3f5fb50b3d5 | -8.5797 | -44.5783 | 2026-09-17 17:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| e6bf6716-7d14-3021-9537-5233bd1675a9 | -8.8647 | -45.8693 | 2026-09-17 17:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.0 |
| b56b80d7-1308-31af-a0f2-17a17dcf5b9c | -6.7094 | -59.443 | 2026-09-17 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 150.0 |
| eb39e725-f6a1-3ca7-aacd-99ce6e0faaf4 | -7.8227 | -44.8175 | 2026-09-17 17:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 6ce1c351-0069-3d89-969a-5d1307fa1eed | -7.8033 | -44.8651 | 2026-09-17 17:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 248.0 |
| b5c993f9-cde5-3827-b164-18579246ec5a | -7.8036 | -44.8422 | 2026-09-17 17:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 6f673dd4-4844-3a7f-b136-aa5bf69e312f | 2.1818 | -50.8985 | 2026-09-17 17:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f57c80bd-c9e9-3e55-b76c-e56f2fb4ba96 | -6.0168 | -52.182 | 2026-09-17 17:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 5b23dfde-cb84-338b-bc35-026401129322 | -6.7463 | -59.4416 | 2026-09-17 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.2 |
| abd3fef9-12ac-343f-a1ab-d629e420e1c0 | -6.7279 | -59.4423 | 2026-09-17 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| f203d414-17bc-3032-8acc-e94a6a87adc9 | -6.7816 | -59.7288 | 2026-09-17 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |
| c42fe4ee-85cf-3ee6-8c13-efe91bfa8fe9 | 2.2003 | -50.8773 | 2026-09-17 17:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 117.6 |
| fe4c485b-5ede-33a4-956d-c215aba9cd03 | -7.8224 | -44.8404 | 2026-09-17 17:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 183.1 |
| c364cd25-d59c-302e-9ad6-0773ae208914 | -10.1168 | -45.6346 | 2026-09-17 17:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 254.2 |
| d8d2a3e3-7436-3e19-9907-1bba368d21bd | 2.2187 | -50.8769 | 2026-09-17 17:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 88004981-e5fa-3649-ba0c-e4ce05ff5e50 | -9.7877 | -46.1045 | 2026-09-17 17:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 65dc998b-c5e7-338f-bb2a-a55b86ce8779 | -8.58 | -44.5552 | 2026-09-17 17:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| e32767ed-b198-3f00-b3bd-ded77e95d052 | -6.6952 | -58.7097 | 2026-09-17 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 0c2aab88-e737-3c2a-8901-2bcaad68d18e | -8.5611 | -44.5573 | 2026-09-17 17:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 3d065c7a-1101-396a-8548-cec193fa64c7 | -6.7464 | -59.4223 | 2026-09-17 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 143.0 |
| f9824a3b-1de5-3046-a9a7-bca6d1ea1efd | -6.6766 | -58.7299 | 2026-09-17 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| d3c360e9-2255-38b0-9e1f-15ea0a67bd94 | -6.7684 | -58.8035 | 2026-09-17 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| b0ea2c1e-ea82-3f41-adc3-5a861f6a391a | -9.7497 | -46.1089 | 2026-09-17 17:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 3189069b-2ae7-384f-94f6-a368e7d680b5 | -6.4401 | -58.1575 | 2026-09-17 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 0e554ae3-035d-3ed8-8663-bc8447ebb91a | -8.8644 | -45.8919 | 2026-09-17 17:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| d66952d2-9fb0-348b-b5ba-7f152596ec6d | -10.9298 | -48.3717 | 2026-09-17 17:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 22b8be98-2d9e-31fa-b56d-2f01a997a343 | -7.8221 | -44.8632 | 2026-09-17 17:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 191.9 |
| cbb2fdd9-4dc3-3f42-a4f0-a405351c7c8d | -5.144 | -55.9345 | 2026-09-17 17:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 47702961-a3b2-336d-826c-af7be3d314ab | -6.6767 | -58.7105 | 2026-09-17 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 0f692ac8-1ce6-32b5-9692-777c267c98f1 | -9.5512 | -45.4296 | 2026-09-17 17:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 743edd53-88b8-333f-be84-ebbd63b0b308 | -9.8322 | -48.3417 | 2026-09-17 17:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 04fe85c6-48cd-334f-9907-721a598a015c | -9.8884 | -48.3794 | 2026-09-17 17:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| c217dee2-79c0-30fa-8a02-4d12a5dff928 | -9.8319 | -48.3636 | 2026-09-17 17:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 153.7 |
| a4a8f7ec-09e8-3083-b8c6-839060c5dd4b | -6.1478 | -57.6825 | 2026-09-17 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| c873e725-ccf4-3532-b5da-f07f453c68b9 | -7.5203 | -44.938 | 2026-09-17 17:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |


