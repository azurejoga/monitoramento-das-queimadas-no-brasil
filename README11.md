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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09ede0a1-1a83-3a9a-bbc2-22478bb80529 | -8.33332 | -48.00787 | 2025-05-17 04:38:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c3353c2-c303-30ab-9a58-b318ebc23296 | -9.56525 | -44.45976 | 2025-05-17 04:38:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e705c2d0-6d77-3e17-b214-af75ed8a54b1 | -9.79633 | -56.13166 | 2025-05-17 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e44890d-6598-351b-b675-e3d06cd9094d | -10.39278 | -57.55265 | 2025-05-17 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d47f3cc-f217-381d-b3ae-1efef386fe2d | -9.21403 | -49.67709 | 2025-05-17 04:38:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c31fec48-e737-3993-902d-3d66ef226601 | -7.30941 | -43.23858 | 2025-05-17 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59184caf-6608-38eb-994d-080454f1f07d | -7.08125 | -44.91719 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57ee86f4-7152-34fc-bc3e-3f6f81ab99de | -11.41661 | -54.32376 | 2025-05-17 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| db18f82d-2081-3eef-bba2-61420eed3202 | -9.54282 | -47.66883 | 2025-05-17 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b029a35-1ab0-38bb-af52-64b4da873d3b | -13.30346 | -45.38213 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 399e92bb-ba61-37d4-9210-4c81e086f607 | -9.36509 | -48.4011 | 2025-05-17 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb77df65-e2e1-3aed-8b0d-b050d29222d7 | -13.05021 | -47.82447 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60d99677-a01b-3803-bb0a-670ffcc2adc5 | -9.31405 | -44.82972 | 2025-05-17 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8489187-3167-363e-900f-146ca64da24e | -13.31018 | -47.46772 | 2025-05-17 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a04ce26-b24c-30f0-929e-ed24c4b2ca4f | -7.23054 | -44.71173 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 024e5f42-cf45-33a9-951d-b7d7028279e5 | -6.71602 | -42.13733 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| ec6ead22-54fa-3cfa-bbc4-6ec685630f9d | -9.83615 | -55.13363 | 2025-05-17 04:38:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| edbbbdd2-6d9e-3d26-8673-2406f7117c97 | -9.79913 | -47.73868 | 2025-05-17 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 700a55f4-c3c1-360b-877d-e4fbef48372b | -13.31229 | -45.37952 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8380e10-ff32-39d8-95f7-344c74ad2af2 | -11.33757 | -46.50932 | 2025-05-17 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d562fe7-f7c9-3916-bc46-0826f659d823 | -7.71653 | -46.29318 | 2025-05-17 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c5f6238-f6ad-3416-81c6-5d55a76ec7ff | -11.16355 | -48.68004 | 2025-05-17 04:38:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5788a51-68e5-3824-889c-b4a1e1c50f68 | -13.31074 | -45.3911 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33650ebd-b14a-3768-bc26-aee1dd8def09 | -13.18015 | -47.80026 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 506a6d44-5aa0-3951-a667-5eced43a6d86 | -11.57747 | -47.6089 | 2025-05-17 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3c8d780-d655-3d26-ada8-d98e12331c4e | -6.72013 | -42.11974 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bde530e2-dcdb-3405-91e5-ad2bceebda6f | -13.32323 | -45.39287 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c42962e1-e375-3176-a658-26bb75c6a46f | -12.34961 | -49.96498 | 2025-05-17 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cab15f20-a248-3ff3-bb83-9d305544d654 | -11.64357 | -48.0191 | 2025-05-17 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 540c9d05-dff8-3e27-a8ed-24ac80063b2a | -6.72147 | -42.133 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a5c1bc95-418a-3659-be3e-435ffea7b1a1 | -13.05139 | -47.81623 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 681fbae1-2da6-32bf-bed8-3be861577748 | -11.15787 | -48.67152 | 2025-05-17 04:38:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d3bdf17-cd73-38da-b6da-18e574790f9d | -7.90297 | -44.47945 | 2025-05-17 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aba3d5d-0648-34e5-b890-5c6e1b612eba | -11.66385 | -54.94666 | 2025-05-17 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd95309c-72c6-3d44-b01d-70e7b3a0daf9 | -19.12517 | -54.45544 | 2025-05-17 04:40:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6142e257-b89d-3794-b7cf-bdc765f76d04 | -13.81948 | -59.66433 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8c31ff1c-9cef-346e-aea3-527488a1167e | -15.26609 | -51.48066 | 2025-05-17 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| abba5739-fcc7-314b-8664-2dd10d1591dd | -17.75623 | -56.31198 | 2025-05-17 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 41bf0af4-74a9-3920-b9c3-ea6bfec2db3b | -20.51438 | -47.35893 | 2025-05-17 04:40:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23cae2dc-c91d-32a6-afde-baad2f0b9822 | -12.453 | -57.19544 | 2025-05-17 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23f2e9b3-7b30-32c4-a287-bece9d81ee97 | -12.45737 | -57.19626 | 2025-05-17 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ed0a013-74ec-3311-baa1-89972841d6d2 | -19.05942 | -53.45759 | 2025-05-17 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f0176db7-84d6-3046-bdc7-57028fa91aad | -12.68371 | -58.13139 | 2025-05-17 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4ebd56e-fdd4-3cb5-8fb3-98eb9b0032ff | -19.06672 | -53.45507 | 2025-05-17 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0fcbe0a8-828c-3092-b044-4cdd98b27f6e | -17.76002 | -56.31273 | 2025-05-17 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 57a2d99c-8d51-33f3-9164-24705d61f36e | -15.51685 | -53.50795 | 2025-05-17 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3533c4fa-5ffb-308c-b4d5-8dea2a01bc71 | -13.50296 | -47.39709 | 2025-05-17 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80a37208-f1c5-3ffe-ae48-57acc36f55f0 | -14.00814 | -53.01696 | 2025-05-17 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4efc945-639d-312c-9738-4a843185fe5c | -13.85341 | -59.72623 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1446843-c0cc-357e-99a4-0cbdfceec49a | -13.97715 | -56.79885 | 2025-05-17 04:40:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58315381-d7f4-3b6f-b727-baac2489d4cc | -18.95566 | -52.24166 | 2025-05-17 04:40:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d43cea59-2dca-3f4e-b3fc-d92efa4abbd2 | -14.0182 | -55.12318 | 2025-05-17 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91d87167-cd73-3b1c-881f-f4b0f06eceb2 | -17.75962 | -56.31025 | 2025-05-17 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 87955923-6918-37e8-9621-35c63a9358f3 | -13.14009 | -56.80505 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bf915c88-eaf4-3953-b46e-1d5026f10723 | -19.12109 | -54.45868 | 2025-05-17 04:40:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ef79927-21d8-3b50-aa7a-52cc8d649fc5 | -20.7648 | -46.76845 | 2025-05-17 04:40:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ae777030-ec7c-3726-bdad-b0651510f1d9 | -13.39904 | -56.91333 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| db10a8e9-c548-3351-bd04-5595701624cd | -12.64886 | -57.18912 | 2025-05-17 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2990d56a-813e-3db8-9de5-0bf18e8c933d | -13.84899 | -59.72211 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 370332ee-c1c2-34e3-baeb-17a553901f92 | -14.02036 | -55.13307 | 2025-05-17 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a269afea-1454-3ae2-bfff-e4e3d6da1317 | -13.50227 | -47.40186 | 2025-05-17 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4262fe65-b654-3148-9508-561267fa8472 | -13.85219 | -59.73238 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfe3ab32-b3f8-3114-8bcd-618d7fac36e4 | -18.38698 | -44.18853 | 2025-05-17 04:40:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ac377cb-2484-3dd4-b0c3-33f5b6ca50bc | -12.45658 | -57.20062 | 2025-05-17 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3965ab28-1073-3c78-ba39-26ab89e4b9ea | -13.13938 | -56.809 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8da3ad88-675e-3680-9533-4e20b1949881 | -18.38636 | -44.19401 | 2025-05-17 04:40:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c79bac5-ae9b-379d-9e07-5d99e62e6560 | -20.37334 | -48.08051 | 2025-05-17 04:40:00 | NOAA-20 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d1a04b8-aa0c-3f86-968a-6cbde8a3cc7e | -20.25333 | -49.34152 | 2025-05-17 04:40:00 | NOAA-20 | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 26b98827-ed83-3abf-a846-e9c0e49b1d6a | -14.01741 | -55.12777 | 2025-05-17 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12b92a12-f6cd-35b7-80f4-ad61a167b2c2 | -14.06423 | -45.42242 | 2025-05-17 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b38143b-878e-33f6-b2bb-546efa398a4d | -15.09031 | -52.84221 | 2025-05-17 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b025ed1a-b748-34a9-83a4-272d78cc10a4 | -13.14358 | -56.80984 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cc627e47-1b97-3078-964a-147443855471 | -14.01957 | -55.13768 | 2025-05-17 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9969d85-b6df-3ef9-9288-2b997c935be8 | -17.72622 | -54.08638 | 2025-05-17 04:40:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3744fe4-6b6f-3743-b196-aa4c031e91b1 | -13.14429 | -56.8059 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c20c720e-6077-32b2-8f5f-8ed77be53f0c | -13.145 | -56.80196 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6873a32c-3ace-3f94-9a22-74f3e29618d8 | -16.02968 | -43.67825 | 2025-05-17 04:40:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fac7890-a024-3cf4-9649-0f934abb282b | -13.04151 | -53.72093 | 2025-05-17 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fcad924-9902-3b9a-b42b-8d72c1f6c5da | -13.3906 | -56.91174 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ff7efd25-568d-3d11-a04c-bd5898e81327 | -11.64786 | -58.26276 | 2025-05-17 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33f6d1a2-5d2c-3849-bc4a-8f7fccc9e3bc | -19.06003 | -53.45385 | 2025-05-17 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0465c2f2-3a40-3946-a6aa-4b811ee8b93e | -13.82944 | -59.6667 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 106e07ed-51e4-385d-bae4-57b4c862340e | -18.8759 | -53.33345 | 2025-05-17 04:40:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 543af94d-787d-33a3-8135-5c16b81f778f | -13.83443 | -59.66786 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 549bcfc9-2877-3c68-ad2d-234d4350406a | -13.8528 | -59.72931 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6767c6dc-061a-36ea-a439-bfadd98b94a0 | -18.65964 | -47.85714 | 2025-05-17 04:40:00 | NOAA-20 | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28b6f701-f3fb-3d26-9c55-fdacf18583a0 | -16.03386 | -43.68435 | 2025-05-17 04:40:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c23bd78-708e-38bf-bffc-32913a9fb09a | -12.64375 | -57.19248 | 2025-05-17 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c290f1f-f4e8-3504-8f9c-c9e5840a2fd5 | -18.65773 | -47.8544 | 2025-05-17 04:40:00 | NOAA-20 | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da3ab795-aa03-35ec-89eb-e6d166fc4d57 | -13.84838 | -59.72519 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89af6ca5-f830-38b9-abaa-f23d87c46c66 | -13.85368 | -59.73111 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 552235ff-fbcd-3764-a5b1-2fa472967993 | -15.26502 | -51.46584 | 2025-05-17 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44e5d759-3441-3d33-9407-8239a2b2de49 | -13.66774 | -52.19588 | 2025-05-17 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a2faaf2-8ff8-37ae-96fc-b578fa510264 | -19.0661 | -53.4588 | 2025-05-17 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fc63936-ecf8-3e74-8b9c-cf80693b5a5c | -18.95177 | -52.24472 | 2025-05-17 04:40:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dadcc05c-0b2c-3bad-96fc-e8baee9bd781 | -17.7786 | -42.80812 | 2025-05-17 04:40:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b93d5945-c99b-3c4b-bb74-69fbcb687e96 | -14.65782 | -50.19409 | 2025-05-17 04:40:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e21d6229-ead5-3846-b1df-8246d5fcfc04 | -14.06528 | -45.4145 | 2025-05-17 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f198ad32-3c10-354f-af17-6c66fb739eb2 | -13.58452 | -47.37213 | 2025-05-17 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3b34d5e-3c97-32d2-800c-84fca1fea442 | -13.14778 | -56.81068 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README12.md)
