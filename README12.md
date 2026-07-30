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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3238e140-fa51-30bb-af82-09ddf3ed4eae | -11.41804 | -50.08906 | 2026-07-30 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54bd3132-3049-3608-832c-f32ec0aba7cd | -9.479 | -57.31687 | 2026-07-30 05:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9ac2653-fe28-344d-b31d-cecbe56dc40c | -10.07561 | -60.50248 | 2026-07-30 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6eded50-a31b-3c79-ad2c-2166f14b1303 | -8.82737 | -66.7545 | 2026-07-30 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b83f6d4a-e481-3157-b887-59198333bbab | -9.78656 | -62.723 | 2026-07-30 05:36:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acefca93-e9ff-32f1-af17-f836f5623d8c | -8.82323 | -66.75374 | 2026-07-30 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02b2eefd-5712-3b2b-b422-20334abda333 | -9.57461 | -60.63161 | 2026-07-30 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 796d52a0-134a-3433-bad9-514e758c26df | -9.48212 | -57.32217 | 2026-07-30 05:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67b9e3cf-a02a-3836-b9b4-9fd6156b9d98 | -9.47556 | -63.27771 | 2026-07-30 05:36:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64c2de88-4978-3dcd-bdca-a15f87ef607b | -12.12322 | -62.04745 | 2026-07-30 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca815b18-4efd-383b-b5fa-81d228488dce | -9.47152 | -63.28087 | 2026-07-30 05:36:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06c2df48-7db1-3bdf-9933-ed698b1727ab | -12.12266 | -62.05097 | 2026-07-30 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a835858-c6f1-3e8b-9dea-835560b97fd3 | -11.41172 | -50.08825 | 2026-07-30 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3891a8a9-ad7d-3521-b4eb-5f1ed44cfff3 | -8.91816 | -65.00841 | 2026-07-30 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff5b86ea-65f3-3836-92bf-30aa3a2fc3cd | -18.80839 | -53.14637 | 2026-07-30 05:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f434380b-51c6-3500-a55d-134cada71634 | -20.59783 | -57.24657 | 2026-07-30 05:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca56370c-7129-3d0b-8306-3fdd34301928 | -18.47678 | -51.73095 | 2026-07-30 05:38:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02020a58-7e51-3edd-a7d2-f701b935e618 | -18.47727 | -51.72593 | 2026-07-30 05:38:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89886ea9-00b0-32b0-b2a1-b810a0de297a | -20.78481 | -57.87511 | 2026-07-30 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 24aa816c-1669-33f1-a8bf-11aa34e63e56 | -20.57282 | -57.26662 | 2026-07-30 05:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| be49057c-1ae8-3b35-8c68-c56d94726080 | -18.80227 | -53.14985 | 2026-07-30 05:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03cd1578-8d71-3d5b-b160-62cd9fd47b10 | -18.47055 | -51.73053 | 2026-07-30 05:38:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e61bcd6c-8201-306c-925b-e81c6ceffdc5 | -10.9397 | -43.0593 | 2026-07-30 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 76031648-4ee3-3593-802f-3adb0a1adbda | -10.9397 | -43.0593 | 2026-07-30 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| a2a4f459-47f3-33a0-9efa-3854382b047d | -9.11283 | -68.48773 | 2026-07-30 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97023d5a-2faa-3bc8-8586-698e34ba40f7 | -8.91471 | -65.00126 | 2026-07-30 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98b3a1b3-118f-3c65-8164-e976eab6f4e3 | -7.01737 | -71.68316 | 2026-07-30 05:53:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e8a3952-a4fb-37e9-bf50-e081cf7eb9ca | -8.82715 | -66.75262 | 2026-07-30 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f178d48-4f10-3d18-95a5-784eb6db06c5 | -8.91763 | -65.00576 | 2026-07-30 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 563374b3-775c-31fd-8295-fec54647f3ce | -9.4727 | -63.27974 | 2026-07-30 05:53:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f7fbeee-0ca0-393d-b988-7c63bbfe23da | -9.49758 | -66.7162 | 2026-07-30 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2006c9e-bbc8-3855-a30b-2afe547648c8 | -8.82382 | -66.7521 | 2026-07-30 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3763b4ad-51f0-3193-8d3b-170267f7ea01 | -8.9153 | -64.9973 | 2026-07-30 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4379859-93df-376e-8200-628e3d54a737 | -9.92168 | -67.04766 | 2026-07-30 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bbff34e-e434-3e1c-ac1c-ae985ee8c8fa | -8.90294 | -68.73743 | 2026-07-30 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4ace09f-cd07-32b5-969d-c74920592363 | 1.76947 | -60.22913 | 2026-07-30 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 052e83f8-9730-394a-85a5-779a9b2e323d | -8.82659 | -66.75614 | 2026-07-30 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d8b3f61-53b3-338b-8864-e5a0dbff166a | -9.49704 | -66.71976 | 2026-07-30 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0e81223-76d3-375a-aa07-e61fc5cc9cef | -9.92113 | -67.0512 | 2026-07-30 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1daf3455-37f6-32a2-8542-87b82fb005f3 | 1.77004 | -60.23262 | 2026-07-30 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6248d942-1333-3cbd-aee7-08d33640e40d | 1.76858 | -60.23326 | 2026-07-30 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee5cfce4-8790-30b3-a187-d3d46b96a3b3 | -9.64074 | -67.21565 | 2026-07-30 05:53:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b58cffd6-3b8c-31df-87de-6636b755836e | 1.76803 | -60.22977 | 2026-07-30 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a0057e5-8bde-3b74-9f70-c4efc0bce6bc | -12.1249 | -62.05022 | 2026-07-30 05:55:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdb0ba46-b689-303e-9136-e12c33b38b73 | -13.05599 | -60.65739 | 2026-07-30 05:55:00 | NOAA-20 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e33875a-2932-3677-8c2a-6472e406547b | -6.64991 | -59.11056 | 2026-07-30 05:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e580998-71da-373b-b939-c5ab039a6915 | -6.65485 | -59.11125 | 2026-07-30 05:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 46d34614-4a4a-3e7c-8b47-32692559c26c | -6.65565 | -59.10555 | 2026-07-30 05:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 37f34ceb-e40d-3cf0-b25f-820e7bbd6a48 | -11.97489 | -63.166 | 2026-07-30 05:55:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86ff9042-b04c-3798-ae79-0f479a54d560 | -6.85932 | -56.53271 | 2026-07-30 05:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c75616dd-646a-3454-bcb9-ca6c18d04351 | -6.85341 | -56.53207 | 2026-07-30 05:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32ba1736-bd57-33b7-a2c1-4204686a288f | -10.9397 | -43.0593 | 2026-07-30 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 3bfaa3e6-aa83-35d4-9265-7c275835b088 | -10.9397 | -43.0593 | 2026-07-30 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| d2d33147-1169-3da2-8d3c-b8f0aa3797aa | -6.57087 | -51.06441 | 2026-07-30 06:12:00 | AQUA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| c35b8f56-cc10-3835-88bd-9a09269960e4 | -4.02978 | -43.26636 | 2026-07-30 06:12:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6ab1f155-2dd2-3766-ab8d-a25121225738 | -13.31205 | -43.59124 | 2026-07-30 06:14:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 95cc38fc-feb8-3309-8fcf-34cac3280b9b | -18.22748 | -42.20885 | 2026-07-30 06:14:00 | AQUA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 5fac2eee-062e-3660-8f5d-9660f3955fd8 | -10.93536 | -43.04984 | 2026-07-30 06:14:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 3f982f18-4334-32ff-bbb5-39ee11ba907f | -10.93387 | -43.05923 | 2026-07-30 06:14:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| a83a7f09-8bc8-33b2-9c54-aa4576717a9b | -18.22886 | -42.19938 | 2026-07-30 06:14:00 | AQUA_M-M | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 1c9447eb-89bf-32fa-9b8a-09de139d05d0 | -18.23635 | -42.21033 | 2026-07-30 06:14:00 | AQUA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| cffd60f0-e830-31ec-b5ba-9527d2047932 | -22.75837 | -43.74067 | 2026-07-30 06:16:00 | AQUA_M-M | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 3fa1180f-8396-3031-9fc3-61d1456f828d | -22.75977 | -43.73112 | 2026-07-30 06:16:00 | AQUA_M-M | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| cce2904e-680b-3f03-9d29-2082fe4a1905 | -10.9397 | -43.0593 | 2026-07-30 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c2929c28-0459-3367-86d4-2b0ed9fd34f8 | -10.9397 | -43.0593 | 2026-07-30 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| da237a97-fb0f-3644-935e-2cbe8a40099a | -10.9397 | -43.0593 | 2026-07-30 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 81b9c79f-e529-3736-916d-af03b2a5616f | -10.9397 | -43.0593 | 2026-07-30 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| becdc2d6-956b-3995-baaa-49620a8525e9 | -10.9397 | -43.0593 | 2026-07-30 07:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| dfdd136a-5286-393e-a291-800cecc2c883 | -18.2374 | -42.21 | 2026-07-30 07:10:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.9 |
| d0089110-0420-3e24-8e1a-cf0793448934 | -18.2374 | -42.21 | 2026-07-30 07:20:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.8 |
| 6982a97c-0a1c-37e1-bde1-61f142162daa | -18.2374 | -42.21 | 2026-07-30 07:30:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| 19d3131a-97e6-3f4b-9fc4-a1ea378f25b4 | -18.2374 | -42.21 | 2026-07-30 07:40:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| 4fe6d185-a7d8-3ccf-944a-8a6d34f47439 | -6.65166 | -59.1012 | 2026-07-30 07:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 19e058fd-3fbb-3448-9f00-6e9b802f6447 | -6.64798 | -59.11315 | 2026-07-30 07:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| bb03add0-cf9b-3362-a1be-e93e2eee5ae6 | -4.88961 | -37.49812 | 2026-07-30 11:00:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b5a3eeab-7d0a-323d-8923-07649c35ba55 | -6.98843 | -38.13639 | 2026-07-30 11:00:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c5a119b1-878a-3407-a4a4-c82f24f47e8f | -4.99166 | -37.23149 | 2026-07-30 11:00:00 | TERRA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0f432241-789f-32cb-92f3-0fa47bd5fc2c | -6.97848 | -38.13508 | 2026-07-30 11:00:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 20.4 |
| f8ff1d7b-339b-3e39-8635-e0ee7516049e | -8.47115 | -36.67244 | 2026-07-30 11:02:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8c381c3d-341d-3f0d-b801-1edfa25fdb16 | -8.46978 | -36.68174 | 2026-07-30 11:02:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 98c38fd7-8529-34a0-b164-8c9b3c9476bc | -17.85603 | -45.36036 | 2026-07-30 11:04:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 36.1 |
| c95986a7-670b-3aa4-a105-3175b1495077 | -17.85967 | -45.36701 | 2026-07-30 11:04:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 072eaba7-2020-3944-b041-f98dbbebe70f | -18.22892 | -42.20079 | 2026-07-30 11:04:00 | TERRA_M-M | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 43c8993c-6636-374e-b19b-9ca0f7a86f0d | -6.65991 | -59.10769 | 2026-07-30 12:38:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d698b370-1cf5-3f88-a6d6-62d60ecce41c | -6.57811 | -51.11575 | 2026-07-30 12:38:00 | TERRA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| ed4d772e-8a1d-3835-be57-ae8bd67af133 | -11.9296 | -43.4288 | 2026-07-30 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 1ed0eac0-d019-33f7-bf17-f6e58f9b05db | -13.45559 | -51.50212 | 2026-07-30 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 253e34ae-214d-3f0e-af64-707f077d46ea | -13.46416 | -51.49635 | 2026-07-30 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| b9e9f17c-7d1d-31b8-b42c-bb8adb3f702f | -12.00161 | -56.08093 | 2026-07-30 12:40:00 | TERRA_M-T | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 86511b63-3d35-3e7f-ae7a-6133d1c8b652 | -13.45203 | -51.5367 | 2026-07-30 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| c82a2e29-82c7-329a-ad61-3f046f0abbe1 | -13.46034 | -51.53089 | 2026-07-30 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 7a534c73-b858-31a9-a4c4-60a7002c3df3 | -12.6186 | -44.6116 | 2026-07-30 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c8111c18-2708-383c-9b6a-8cd9fd8d3e83 | -4.0333 | -43.263 | 2026-07-30 12:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 51129af6-45dc-3b41-b000-388745e6d99f | -11.9296 | -43.4288 | 2026-07-30 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 5fa62c2a-caf9-31be-8d9b-dd9a323f987a | -12.6186 | -44.6116 | 2026-07-30 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 460e3e15-d0ed-302a-995a-2cbd6ac960bd | -11.9104 | -43.4319 | 2026-07-30 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| fe59db94-4a16-35f6-a7d3-8200f4e1d696 | -11.4169 | -50.0948 | 2026-07-30 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5601692f-7515-3ae7-aa37-44739f50a687 | -12.6186 | -44.6116 | 2026-07-30 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 3455234d-79bb-3b6b-8407-688d0eac3396 | -11.9296 | -43.4288 | 2026-07-30 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| a7f5f164-c816-3222-bf62-927667e5c489 | -11.4169 | -50.0948 | 2026-07-30 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |


[Clique aqui para ver as próximas entradas](README13.md)
