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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed5ae498-932e-3070-979d-ecae7c9bb34d | -16.28121 | -58.67182 | 2025-05-23 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 905b61fc-3315-3d71-ae3d-7842e9e15916 | -19.73426 | -54.51427 | 2025-05-23 05:21:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 350a30ba-d4d0-39af-8a65-4d7c6952f21b | -20.85714 | -53.74682 | 2025-05-23 05:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e512caa0-5742-3e26-b3db-59f189f2b8d6 | -15.63974 | -59.71833 | 2025-05-23 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c52e44ca-6535-3afe-aef0-144f3fbf8dbb | -14.16459 | -59.99047 | 2025-05-23 05:21:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8320f6c4-dc96-381a-9e16-efe443ee3b7b | -16.01665 | -53.20122 | 2025-05-23 05:21:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6edfd06-a211-3626-8f0f-992d49465bdd | -20.85215 | -53.7461 | 2025-05-23 05:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6d19c8f2-6e6e-36f8-b722-1c6acc60f965 | -20.95038 | -56.59355 | 2025-05-23 05:21:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1222c680-f287-3132-a26d-0eca6219a9c3 | -13.86222 | -59.72233 | 2025-05-23 05:21:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5327a2e2-b94f-321b-b4f2-6460588c9092 | -21.72414 | -55.37424 | 2025-05-23 05:21:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 031ed66e-3459-3e32-b9ef-587047a22af9 | -17.34147 | -51.91024 | 2025-05-23 05:21:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77147c68-7ac4-33f3-aac5-877c223b1578 | -20.95354 | -56.60219 | 2025-05-23 05:21:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9f37c55-4a57-3b79-8243-cf0f3782029a | -13.85834 | -59.7254 | 2025-05-23 05:21:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e8059a0-3bba-3a0c-95dc-24ae1e7c2537 | -21.72016 | -55.36869 | 2025-05-23 05:21:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3288b67d-bbf5-37ee-b425-b443518a48c0 | -15.62729 | -57.30772 | 2025-05-23 05:21:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c1a9717-4c3c-3128-aaf4-0dea40f4c3b8 | -20.94671 | -56.58902 | 2025-05-23 05:21:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65ec5174-6f66-3690-bf57-b856c2d5b0e2 | -19.79457 | -53.83627 | 2025-05-23 05:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae28c865-68d2-3906-bd73-620d8e6fffed | -17.34185 | -51.90678 | 2025-05-23 05:21:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7242a708-c54b-3ff3-a4b0-e66055fec64e | -19.79947 | -53.83677 | 2025-05-23 05:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6f65c35-b601-3e7b-9408-bdaa7609ba32 | -16.28596 | -58.67119 | 2025-05-23 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0e00219a-8c8c-3a1c-9c8c-75e2598f8aaa | -20.85152 | -53.75201 | 2025-05-23 05:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e71ab651-fa7c-3bc9-bfa0-46491e26cdde | -22.48321 | -53.58118 | 2025-05-23 05:23:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 48ca3e6c-6d98-3c10-ba9f-4752622577e7 | -7.0695 | -44.9335 | 2025-05-23 05:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 93c56b38-c251-379d-a463-d9f1e3f219f6 | -6.2224 | -43.3693 | 2025-05-23 05:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 786d4dc2-187f-3299-a877-206308e22d8d | -13.9818 | -56.0151 | 2025-05-23 05:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 051e3689-94c9-31f3-9440-658007edcab6 | -6.2224 | -43.3693 | 2025-05-23 05:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| e580168a-9b6d-38d6-9b52-15a5dee379f9 | -13.9818 | -56.0151 | 2025-05-23 05:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| b2c4ee28-f3eb-3676-beee-ca33ee984804 | -5.57084 | -45.19026 | 2025-05-23 05:42:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e028f843-6105-3c33-8e7a-f624ccbd322a | -5.97677 | -43.75341 | 2025-05-23 05:42:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 18469525-52ae-39bd-890c-4cab31fc9c02 | -7.06845 | -44.92687 | 2025-05-23 05:42:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 330eb23e-439c-36a1-9e74-5188df76bf8f | -5.57978 | -45.19155 | 2025-05-23 05:42:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 0e908f77-45b0-3d07-ae42-696df0f5f093 | -7.05933 | -44.92544 | 2025-05-23 05:42:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 045a9b4d-67fc-3471-848d-ec5ca1f9ad32 | -5.57843 | -45.20065 | 2025-05-23 05:42:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 5f6d0310-6ab7-37ee-804d-4ead8be5407b | -6.23081 | -43.34595 | 2025-05-23 05:42:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5d82caef-e6a2-35c8-9217-012796047855 | -6.2275 | -43.3686 | 2025-05-23 05:42:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| f083cc7c-9d16-3bf9-b704-23f3ba20e6cf | -5.78291 | -43.61584 | 2025-05-23 05:42:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c356cc87-0d0f-3017-b844-9c53cbe005d3 | -6.22914 | -43.35735 | 2025-05-23 05:42:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 68cd70c7-102c-3021-bc27-3e3c23046219 | -7.06707 | -44.93632 | 2025-05-23 05:42:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 35f0e9f0-d315-35a8-83f9-d317d0d51440 | -5.56949 | -45.19935 | 2025-05-23 05:42:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1fbe5c82-16c3-3f1c-8490-f2962346334f | -6.22586 | -43.37977 | 2025-05-23 05:42:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ad8010b3-2735-3d87-bde6-d134bf53b878 | -11.78931 | -44.27169 | 2025-05-23 05:44:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4d1b425e-2a54-3212-96f2-4e9373191e5c | -15.26673 | -51.47155 | 2025-05-23 05:44:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ae74ca9c-2591-3508-8cb7-e7a3ca62e562 | -11.55379 | -47.44491 | 2025-05-23 05:44:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a0e1229-766b-325d-9cbb-9768d03cb0c9 | -12.42134 | -49.97692 | 2025-05-23 05:44:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 80dfbde9-8b14-3989-ae9a-766162257581 | -12.33755 | -49.97832 | 2025-05-23 05:44:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 10c4c35f-77ec-3456-bb81-2d1483b4b095 | -11.78767 | -44.28354 | 2025-05-23 05:44:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 7d8d46f6-d1b1-33aa-a4aa-522229e5400c | -13.77848 | -54.30061 | 2025-05-23 05:44:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d03daefc-e048-38ba-985f-4086faf293a1 | -12.84425 | -47.38988 | 2025-05-23 05:44:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ecd9691a-90ac-3ef3-b744-b3eada9ff1c6 | -14.03808 | -53.37243 | 2025-05-23 05:44:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1a6ee668-45de-3c4e-a0f7-9424e67ad3d8 | -11.77761 | -44.28213 | 2025-05-23 05:44:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 131b7c7f-907e-3837-8852-0d7bd19bd042 | -12.0688 | -47.33356 | 2025-05-23 05:44:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 30d12564-f928-3015-bb3d-56a017d6070a | -12.32664 | -49.98695 | 2025-05-23 05:44:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| fca0f996-3955-39cd-ad77-437785119381 | -12.29005 | -52.49784 | 2025-05-23 05:44:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 5aaa0bad-17f5-315b-bffc-e3bc8959a8cf | -12.41975 | -49.98704 | 2025-05-23 05:44:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c0d5c18-dc5f-37e8-87af-6fbf3f63606a | -12.29246 | -52.48338 | 2025-05-23 05:44:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0b5877c7-860e-306c-8631-168edb13a269 | -11.56259 | -47.44624 | 2025-05-23 05:44:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f04efb8e-b466-34ae-9858-c7d38fbecd48 | -12.06746 | -47.34254 | 2025-05-23 05:44:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| c3005ca0-f398-3daa-bb17-0ded0ef00c38 | -9.95968 | -49.81443 | 2025-05-23 05:44:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b7112e1a-7c73-365e-8045-e9f1318ef655 | -13.97682 | -56.00634 | 2025-05-23 05:44:00 | AQUA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 12c7302b-fb37-36f3-9dca-12a4cbaac133 | -15.26485 | -51.48283 | 2025-05-23 05:44:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 75a945fe-65d1-3954-9920-b15dd1211071 | -9.96133 | -49.80393 | 2025-05-23 05:44:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| e30a883b-fc16-3606-9de4-2cd79018424c | -12.33596 | -49.98842 | 2025-05-23 05:44:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 08741305-5835-3f52-94b5-5c8c5d523755 | -13.77962 | -54.30795 | 2025-05-23 05:44:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| a8fb7017-362e-313f-8bcd-a590aeb38992 | -11.51439 | -48.55605 | 2025-05-23 05:44:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0cc6959b-4737-3759-9067-b29fe722977a | -15.26278 | -51.4768 | 2025-05-23 05:44:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3d130535-fa79-325a-adc3-916c5b48f287 | -7.70858 | -45.65939 | 2025-05-23 05:44:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5a940e37-2e1d-3a12-a3a4-ee129ce2f07b | -12.07628 | -47.34388 | 2025-05-23 05:44:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7ef5a22f-4d8f-30d0-b2c9-1283285f3c0a | -9.86147 | -60.3188 | 2025-05-23 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c4413ee-06f5-3755-8f22-5c9920872013 | -10.99246 | -59.15271 | 2025-05-23 05:44:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a0cd6e4-9f22-3a60-a034-6fa749474292 | -11.29367 | -53.98346 | 2025-05-23 05:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b3e0d0d-e44e-3fd2-84d8-dc3a1d0a17aa | -12.72155 | -54.97847 | 2025-05-23 05:44:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e21159c-25ab-3e8e-982b-d9f6ce54ceaf | -10.31104 | -59.57066 | 2025-05-23 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c46e23ed-2d60-3693-8c50-987e293fe504 | -10.36987 | -57.50092 | 2025-05-23 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f393ef0-b2d1-325c-bbbc-29b121be4a26 | -10.98826 | -59.15845 | 2025-05-23 05:44:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b69157ad-d0bf-34b8-b788-d692a934f2d2 | -12.30208 | -52.49265 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f15b8baf-07f6-37d9-8105-b8ac9eded07f | -10.73145 | -59.32179 | 2025-05-23 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f040e224-b136-34e2-bd1f-a46f08544b86 | -12.28675 | -52.49833 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 459c6214-a01c-3bb5-b3de-4d5727c77a5a | -12.30055 | -52.50748 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e878a81e-b9c2-376c-8330-797c8b10b94e | -11.29204 | -53.98089 | 2025-05-23 05:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c0dab0d-20d2-353d-a1a2-0824330958dc | -10.68186 | -57.60214 | 2025-05-23 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 832541c9-eb39-37c3-826a-02b3238b6f37 | -10.82471 | -56.95573 | 2025-05-23 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22f770a4-06b1-33a0-af80-134f3f7ce226 | -11.8079 | -57.35843 | 2025-05-23 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af0ba0a8-e1f0-3626-836c-ac60f637d71a | -11.29863 | -53.98187 | 2025-05-23 05:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7a86ae1-f3ee-3b6a-b45e-abdd8a38ee1e | -12.72214 | -54.97326 | 2025-05-23 05:44:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4708b762-7367-38de-af5a-44a89c464584 | -12.29334 | -52.49342 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0cef67d3-ee1e-3cdc-97cd-d0de5dbd87f8 | -11.80747 | -57.36185 | 2025-05-23 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4da0530e-385f-36f4-a3f3-bfbe82e7c094 | -12.28525 | -52.49994 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f751220-67a8-36ea-8a75-406b7fc3c504 | -12.29981 | -52.50164 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e45f384-0313-3b0f-9233-5df7cd3c4cb3 | -10.81929 | -56.95485 | 2025-05-23 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8f0e47e-b4d6-334c-b5f5-c499e2022353 | -9.49263 | -63.32267 | 2025-05-23 05:44:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2ec1be2-4827-3ccb-aeaf-374e0fab7d27 | -10.9889 | -59.15356 | 2025-05-23 05:44:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c5dba72-17d3-39e7-8be3-600bbcca7701 | -10.68103 | -57.60858 | 2025-05-23 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 870048fc-a8e2-3763-a483-d1f862af42af | -9.54773 | -63.33381 | 2025-05-23 05:44:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16d2f1e5-9c4b-3875-9a01-e1ccbc0fd7cb | -12.29253 | -52.50082 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d2604d21-2d5f-3ffb-8cbb-dd6622904bb3 | -10.9842 | -59.15294 | 2025-05-23 05:44:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b87ea18-e064-3944-82ec-ae25a6b0dd9f | -10.31165 | -59.56611 | 2025-05-23 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95bb36aa-e9f8-3d9b-adde-1caac637b2ba | -9.86248 | -60.32026 | 2025-05-23 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 264d8363-860e-3afc-ae02-a35e541849c7 | -11.30026 | -53.98438 | 2025-05-23 05:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47b4aa74-e7a0-300a-8756-b0144e9f2633 | -10.68227 | -57.59894 | 2025-05-23 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcae9085-c603-36e4-8f6d-ccac4737e186 | -12.30062 | -52.49424 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README20.md)
