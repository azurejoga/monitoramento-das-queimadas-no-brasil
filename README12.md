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
| 304db087-2673-310f-bf34-e1e29f3e66fd | -20.19263 | -50.49929 | 2025-07-21 05:14:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 403b4106-567a-35f1-86c9-e4ced1d546be | -20.19379 | -50.49954 | 2025-07-21 05:14:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| f51a6637-791b-3f3c-9fff-c36c19396bdf | -15.02601 | -49.25446 | 2025-07-21 05:14:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4f269f7-5e9f-3917-b9be-edaeb71200de | -14.77837 | -47.99427 | 2025-07-21 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9609c9d4-2865-38c8-a325-636bb056abf8 | -20.27461 | -54.80655 | 2025-07-21 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67746c42-2c28-347a-b7a4-ca97b8e9721d | -20.27087 | -54.80201 | 2025-07-21 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b6e7934-15f4-33b0-b432-41827696a505 | -14.76715 | -47.9832 | 2025-07-21 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcd3c6ab-dee8-3c67-9d24-87959f9f8dcd | -13.45476 | -60.97709 | 2025-07-21 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c241338e-abb7-35c6-bcf0-0915f33fbd4e | -20.19417 | -50.49573 | 2025-07-21 05:14:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e57048cb-c3c3-35d3-9337-329df9b05910 | -20.51682 | -54.72094 | 2025-07-21 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27b1a53e-64a5-394d-8bbb-c927e14a5466 | -19.01995 | -54.65825 | 2025-07-21 05:14:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f114abb-5241-3eb2-b3f9-1d9920b203dc | -19.97894 | -54.34266 | 2025-07-21 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6fcbf80-4966-39ee-b2e7-34d760fa8faa | -20.27135 | -54.79796 | 2025-07-21 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7c33503-13ec-36b5-bc9f-b949934ca632 | -20.19821 | -50.49993 | 2025-07-21 05:14:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c7ce79d6-e4d0-3e22-97a3-58e7f698661d | -20.19341 | -50.50336 | 2025-07-21 05:14:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 3347140c-5874-351d-9055-8acda5b83eb3 | -14.77892 | -47.9891 | 2025-07-21 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8fb01a23-333a-3d4c-a36e-57fc2e63dfd7 | -20.19785 | -50.50375 | 2025-07-21 05:14:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 207bd067-605a-3d1d-a580-3658a2bac9c5 | -14.76664 | -47.98805 | 2025-07-21 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51b9d257-11aa-3fd3-a2e8-6aa4804a89b4 | -20.26664 | -54.80152 | 2025-07-21 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d202f92-0283-3011-84c6-b50b7ab539e2 | -20.19299 | -50.49546 | 2025-07-21 05:14:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| bb1ba478-0811-3a80-87b1-1ba6eae9a64b | -24.54763 | -50.79875 | 2025-07-21 05:16:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 27b793cf-5783-3315-9300-20870802b332 | -22.68569 | -50.47476 | 2025-07-21 05:16:00 | NOAA-21 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8f4800fd-3b48-32bb-9b88-5d51b60371d7 | -23.33941 | -51.90384 | 2025-07-21 05:16:00 | NOAA-21 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 273497fd-dc93-3fd3-871c-9050abc757d8 | -23.34005 | -51.90413 | 2025-07-21 05:16:00 | NOAA-21 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 50ef474c-9e0f-324a-96a6-2e71f1771060 | -21.04344 | -55.99099 | 2025-07-21 05:16:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f68a2ba-9b1c-32a7-8b55-f73e64c04045 | -7.2772 | -60.1698 | 2025-07-21 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| fa4bfecc-a0c7-32e9-8957-ff0b304ad329 | -7.2402 | -60.1904 | 2025-07-21 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7c9acd17-1a5c-3ea9-b53e-6757f2d3eeb3 | -7.2957 | -60.169 | 2025-07-21 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 10c2345f-a326-3757-9ef7-29b783831c08 | -7.2772 | -60.1698 | 2025-07-21 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 26fa8751-7738-39a3-bbac-c96d98db24dd | -7.2957 | -60.169 | 2025-07-21 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| bc411eda-41f5-3551-a88a-cdfc1c439594 | -10.73604 | -52.52007 | 2025-07-21 05:38:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 215dbb15-9542-3bde-9c03-85af844d6231 | -7.27873 | -60.18029 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1bc402de-f714-372e-b926-c6ea3731e6d1 | -10.05895 | -64.99626 | 2025-07-21 05:38:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0873b62f-21d2-3579-b55b-3efbd800b89a | -9.42232 | -66.53249 | 2025-07-21 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d5f7599-02ac-3d73-bb0e-c5bdddab64a2 | -10.037 | -59.09887 | 2025-07-21 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 036a54c2-4dcb-3e87-95b6-df52bd4b0d33 | -8.94072 | -62.22153 | 2025-07-21 05:38:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aba3a89f-fc09-38c7-8d9f-339c5bde57d4 | -7.27247 | -60.17705 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c57fa0c8-7021-36ab-8498-dbd995ce6774 | -9.42033 | -66.53301 | 2025-07-21 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 572e41a0-1e40-38d0-8e7f-2983b7137376 | -7.25061 | -60.18977 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27512e8c-4c5b-3c5d-8ac2-e076ebcde1e2 | -7.26754 | -60.17867 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7af0c72f-125d-3a80-afb1-3752ed0a783c | -7.26141 | -60.11834 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a8b5b11-54f2-3549-9851-9e84fe0a0d6d | -10.29465 | -60.54166 | 2025-07-21 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a322aeaf-a3c9-3df8-8f81-186e31207610 | -11.80907 | -56.96593 | 2025-07-21 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 751fbed1-8c13-3809-a595-2f4cd044cc5a | -9.23609 | -63.62275 | 2025-07-21 05:38:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2fce9a0b-9977-38a7-8114-0036f5fcd2c0 | -8.98743 | -71.57592 | 2025-07-21 05:38:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f565f7fd-4675-3a03-934e-d66b58226246 | -7.27942 | -60.17585 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 23236b00-4300-38af-bcf7-91ff6093aef5 | -11.31484 | -55.21912 | 2025-07-21 05:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c282ea2-9f89-3acb-8147-e0e1986b6e0e | -7.27993 | -60.17811 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d221e7e1-e365-30b1-b481-30e20f382ddb | -7.26381 | -60.17809 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1e876f2d-0f98-3958-83c1-51e97d2c55c9 | -7.28059 | -60.17367 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| dbaf3900-762f-31ac-ba96-3e2ca3dfb5f1 | -9.01527 | -59.54355 | 2025-07-21 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c53b000-7412-3bee-88e5-c21615d0d757 | -5.30319 | -55.97521 | 2025-07-21 05:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42fa9aab-abc5-38c9-a08f-98791950c8fe | -10.38178 | -62.76686 | 2025-07-21 05:38:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c847cd8a-e900-38eb-b4f1-ff6a6a3112ae | -10.05839 | -64.99978 | 2025-07-21 05:38:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54157b0f-cb3f-3b3c-bb23-b37a931050a9 | -7.29243 | -60.17097 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 821b2ca9-6e1b-3996-b942-9547de06ada1 | -8.99412 | -69.23476 | 2025-07-21 05:38:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f402508-bebb-3df1-87fa-d672e81513f9 | -7.95534 | -71.45393 | 2025-07-21 05:38:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69f53dcb-7682-3215-a2de-4a461cde0479 | -7.16665 | -59.63881 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50fd883c-81b5-3089-9fd8-5614e790c742 | -7.28124 | -60.16922 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 1edf77e8-2bca-3a05-b3e8-6cac4ecd0343 | -7.28497 | -60.16981 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 52e5c65d-6565-38b2-9fca-f0a8b9246537 | -9.63206 | -61.45678 | 2025-07-21 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d0e31f3-08b4-32f6-9cd1-01ec07e5cc33 | -7.26313 | -60.18258 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7d88b0c9-f949-3357-a144-7f478103f27e | -5.30392 | -55.97007 | 2025-07-21 05:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78db7033-1db5-3919-8be2-40df54d2191a | -7.27555 | -60.18205 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7bd9ed92-829b-3974-9bc4-bde05d9065b7 | -7.29616 | -60.17154 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d49e88b0-e159-3b7e-a5d4-d236e022585d | -7.28935 | -60.16592 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cf0b3123-453a-3449-baeb-01001e29cb13 | -7.95061 | -71.45309 | 2025-07-21 05:38:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0dbdeba-5508-35fb-842e-5c59a8acb6e7 | -7.23439 | -60.19627 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f7f9342e-90e5-3d2c-82bc-448c5f8a88c2 | -7.24183 | -60.19745 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a76fc6f6-a9b9-3c43-851f-f857f23f8025 | -7.23811 | -60.19687 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0b561cea-bead-3515-9ae4-f715bd107584 | -7.26686 | -60.18315 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8b568309-2c9d-3dc9-86de-f98139fec999 | -7.16736 | -59.63401 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 391102c3-1565-3985-97e6-23b0ff3996cd | -7.26584 | -60.11437 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72206af1-6d41-3c1b-980d-c394aae7d826 | -7.2887 | -60.17038 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a031b5fb-b6d3-35aa-ab06-681bdb2fc96c | -7.24316 | -60.18864 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c7e5072c-7100-328b-862b-0a8619314676 | -7.28009 | -60.17141 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d8159974-51b9-3ea5-ba40-6a6d1e775009 | -7.29309 | -60.16649 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cea882dc-5e69-3706-aeeb-0e4bd6281a7e | -7.24688 | -60.1892 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e303ddb9-8248-398f-9dfb-09ece49ad61a | -7.27568 | -60.1753 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| dfda460d-6e9b-387f-a5cc-861ed0b7f196 | -7.2762 | -60.17757 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 300efe2a-6dc7-3e4e-bf03-8b0cd6272f6e | -10.29845 | -60.54221 | 2025-07-21 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b164e15-f315-3c26-8f85-7185247d43f2 | -10.38122 | -62.77061 | 2025-07-21 05:38:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ea5e8cf-2f39-33c9-9693-e3e7afdefbab | -7.26808 | -60.18096 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eec07424-bb0c-39f5-9ea1-a9d62c614d7a | -7.275 | -60.17976 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce7d4c8d-af0b-3f5c-af2b-30822a373c30 | -7.27685 | -60.17312 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| e5204fa2-5d0f-3c31-b227-2cd3da55f9b0 | -7.29682 | -60.16705 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 880377b6-a9e4-3059-91b1-3e1a1876a27d | -8.49471 | -64.03951 | 2025-07-21 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d35d21a-aa89-369b-841c-db70843c6f0d | -7.25873 | -60.18647 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d12d9fc7-6f2c-3876-baa4-90e5215594e3 | -7.26743 | -60.18545 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 805787b2-4a5c-3f1a-92fb-15b7e5e79d87 | -7.23877 | -60.19248 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 382e4541-906f-3fd9-b628-163f8ed84554 | -8.49194 | -64.0355 | 2025-07-21 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 142b0708-d5ab-3300-aaf7-32e0b7308a03 | -10.72958 | -52.51913 | 2025-07-21 05:38:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a4b3f36-a5bc-3570-8825-145d11a1b7f4 | -8.28636 | -71.07334 | 2025-07-21 05:38:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b61e3b6d-1d6f-3b85-8721-bdff1bcb2c5c | -7.28432 | -60.17425 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 45f01c18-5c48-341c-b7b0-1b3424c65ba7 | -7.26245 | -60.18705 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7477f350-7080-3f15-8e15-86ba19b3369b | -7.23505 | -60.19189 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0d3f0441-bf76-3c3b-86c1-3f07e39b08a6 | -7.27181 | -60.18152 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9dea85d1-9d2e-35fb-a5e8-d2d2e96c87bf | -7.1712 | -59.63458 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d9bf05c-ce25-3a07-af0c-b054a4fc7772 | -11.80773 | -56.96526 | 2025-07-21 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5917dae0-9996-391f-8353-7ae150ac5f05 | -8.99352 | -69.23826 | 2025-07-21 05:38:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README13.md)
