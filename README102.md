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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e11f9077-17de-3589-90b4-e08db7c01f52 | -19.08205 | -44.39722 | 2025-09-04 12:19:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1b3c283b-374a-3110-b22b-230d6e393b93 | -16.70069 | -44.97429 | 2025-09-04 12:19:00 | TERRA_M-T | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 59.7 |
| a5a3ca44-0d0c-3987-82bc-a1597d74eb7d | -20.96186 | -44.92371 | 2025-09-04 12:19:00 | TERRA_M-T | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 502167ad-6676-3f29-a213-6d1de1acc1d0 | -17.06343 | -46.44042 | 2025-09-04 12:19:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8a128ae9-a60d-379d-a85f-5d8af468c52f | -17.04859 | -46.49314 | 2025-09-04 12:19:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f0b5c1b1-0bc7-34b8-89e8-8228179884a4 | -17.05675 | -46.43349 | 2025-09-04 12:19:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 7e0f3b37-a300-318c-8cad-0b3c892635fa | -22.66331 | -43.69476 | 2025-09-04 12:19:00 | TERRA_M-T | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| b61be0cc-52fb-3108-89ea-36c1ed43df18 | -21.72797 | -46.15648 | 2025-09-04 12:19:00 | TERRA_M-T | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 9219c0e9-040b-379d-8ed8-4606483b96c6 | -22.28151 | -52.04317 | 2025-09-04 12:19:00 | TERRA_M-T | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.2 |
| 7642e4f1-b437-3820-9172-9eb5fe71c04a | -18.19942 | -49.72279 | 2025-09-04 12:19:00 | TERRA_M-T | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 3f632b1b-f9c8-38d5-bf7a-a08d1447d23a | -22.65153 | -43.69247 | 2025-09-04 12:19:00 | TERRA_M-T | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 68.8 |
| 26fba402-257c-3224-892d-ca554b788f37 | -17.53032 | -49.13832 | 2025-09-04 12:19:00 | TERRA_M-T | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 454a415a-c567-3b47-9b52-3e4ae0c5e85d | -19.50954 | -46.13945 | 2025-09-04 12:19:00 | TERRA_M-T | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c3f2030a-2599-349c-96b5-28c319c70aa2 | -18.93029 | -47.19342 | 2025-09-04 12:19:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 28.6 |
| f2d3250b-9e03-371a-a285-f02423db4cab | -17.52141 | -49.1369 | 2025-09-04 12:19:00 | TERRA_M-T | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 8d1a8f82-33b5-3759-a3c1-ea24ac96af66 | -18.98808 | -44.77116 | 2025-09-04 12:19:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8de38482-7bac-38b8-ab71-09f7ec5737c2 | -21.51332 | -44.991 | 2025-09-04 12:19:00 | TERRA_M-T | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 575b6a15-d654-35e2-9ba5-353e63be86c0 | -25.8008 | -51.14583 | 2025-09-04 12:19:00 | TERRA_M-T | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 414dd405-8ad5-3098-b90a-2ded70a2dd00 | -15.7465 | -53.63734 | 2025-09-04 12:19:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| be80bd48-8957-34cf-84a9-bff9adbfd4ee | -16.7025 | -44.96848 | 2025-09-04 12:19:00 | TERRA_M-T | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 49e48c2d-3c63-3472-bdbd-7a8d803058bc | -16.32178 | -52.9575 | 2025-09-04 12:19:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 251c3412-0f18-3679-90ee-947784771ced | -22.28326 | -52.03218 | 2025-09-04 12:19:00 | TERRA_M-T | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 651fc53c-ad68-3108-a414-5c56a9a3e566 | -22.50408 | -47.68257 | 2025-09-04 12:19:00 | TERRA_M-T | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| cedb5a48-a7e3-3904-88d7-f0ca7aa2884b | -21.24269 | -50.4088 | 2025-09-04 12:19:00 | TERRA_M-T | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| c65c592a-cce2-344d-87f6-8056aef88af6 | -24.95959 | -50.5402 | 2025-09-04 12:19:00 | TERRA_M-T | IPIRANGA | PARANÁ | Brasil | 4110508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 5640c39e-6bd2-36c8-9e6f-ed2b6ce47201 | -18.07223 | -45.97176 | 2025-09-04 12:19:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d063e00c-cad3-307f-895a-bf0b6ecee3d0 | -18.98967 | -44.75825 | 2025-09-04 12:19:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 15e1992f-f391-361f-a634-fae7c343de57 | -21.34819 | -45.60285 | 2025-09-04 12:19:00 | TERRA_M-T | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 18a4f104-3601-3441-b823-3d4e0903077a | -16.3106 | -52.95571 | 2025-09-04 12:19:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0247797c-0b3e-3684-8d65-4689c9d88e06 | -17.5779 | -44.23825 | 2025-09-04 12:19:00 | TERRA_M-T | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 040649a4-085d-30e0-8624-50cf06d974ee | -18.86361 | -47.34606 | 2025-09-04 12:19:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9418042c-0e33-33d6-b17c-6bbf401a710f | -20.09431 | -44.14392 | 2025-09-04 12:19:00 | TERRA_M-T | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 1339efd3-3792-3d8e-8113-62455c97a7a7 | -19.5024 | -43.82428 | 2025-09-04 12:19:00 | TERRA_M-T | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 12345113-a788-39e5-8eb6-670b7e6c5395 | -16.70105 | -44.98008 | 2025-09-04 12:19:00 | TERRA_M-T | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| dd7db7fa-3bb5-3631-9f07-e3ca806208fa | -21.5239 | -44.99239 | 2025-09-04 12:19:00 | TERRA_M-T | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 3762f720-a93e-390b-8485-7ea70fedf404 | -17.05539 | -46.44345 | 2025-09-04 12:19:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 43e55d9a-f6f3-38c3-883e-01715b0fb370 | -20.09305 | -44.1381 | 2025-09-04 12:19:00 | TERRA_M-T | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 0693eabb-ccc0-30ce-9d07-b0166c74706a | -19.74301 | -45.66148 | 2025-09-04 12:19:00 | TERRA_M-T | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| c18ca8a9-798e-3e4c-8811-1e092b80083b | -22.59334 | -42.06994 | 2025-09-04 12:19:00 | TERRA_M-T | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 89a7eb50-1577-3de9-9f7f-9756b5ac52a0 | -20.10219 | -50.01693 | 2025-09-04 12:19:00 | TERRA_M-T | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 882e6121-d24d-3bd8-99cd-4efdb743efd6 | -16.31087 | -45.6892 | 2025-09-04 12:19:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8cba9611-da27-3906-b408-42362dca7240 | -16.30947 | -45.69966 | 2025-09-04 12:19:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e59937cd-9dfa-3821-9518-fd8a2f5fe107 | -19.23888 | -48.67971 | 2025-09-04 12:19:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2d432c15-0c66-36b3-bb4c-dad1d5ac03c0 | -18.57574 | -44.03708 | 2025-09-04 12:19:00 | TERRA_M-T | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c709b643-b2a8-3d33-a4dd-6dd64afae754 | -16.20815 | -48.7234 | 2025-09-04 12:19:00 | TERRA_M-T | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 60300b9b-16db-3f2e-8f76-9c00f767b1db | -11.853 | -51.453 | 2025-09-04 12:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 7a694c0c-71b2-3b8d-b287-f2581e36b996 | -11.8721 | -51.4509 | 2025-09-04 12:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 348d4e5d-dc35-34bd-b877-ba72f4cd7600 | -7.6854 | -48.717 | 2025-09-04 12:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 65d6f6ee-9f1d-3d0a-9dba-7759b1e14370 | -6.2315 | -42.4515 | 2025-09-04 12:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 440.2 |
| 48d15d83-3f4c-3bbd-8aba-862863a758dd | -7.7034 | -48.7803 | 2025-09-04 12:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 023d22c3-0672-33dd-9975-3864782a6a88 | -7.7039 | -48.7371 | 2025-09-04 12:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 93.2 |
| f183d114-f11c-3407-9aed-8fd81ce017bb | -6.3692 | -45.6258 | 2025-09-04 12:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 09613ef7-814f-3838-81cc-68800e659efb | -8.0799 | -45.339 | 2025-09-04 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 0bbbcc37-6eda-3a9a-9f33-b190ef34b7c7 | -6.2318 | -42.4278 | 2025-09-04 12:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 276.9 |
| ec5e5984-7b20-3f15-bc42-917182a68481 | -9.7108 | -48.9636 | 2025-09-04 12:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 5f0ff8a5-9a4c-3346-920e-0f40a8ac38b6 | -7.7036 | -48.7587 | 2025-09-04 12:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 8e83c399-0405-3e8a-a938-8180617a6b0d | -7.6851 | -48.7386 | 2025-09-04 12:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 1cc98359-4fdd-30fb-8d27-926284d83958 | -6.3689 | -45.6483 | 2025-09-04 12:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 0e402e3e-01fb-3672-8917-855f575481f2 | -8.3641 | -48.3334 | 2025-09-04 12:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| f3b01007-001e-3417-824c-fbae1b51ebcf | -4.9049 | -41.7696 | 2025-09-04 12:20:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 157.7 |
| 6ca5a17c-ad6c-3a66-8cd6-497429b1efcf | -6.2127 | -42.4532 | 2025-09-04 12:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 258.4 |
| 22402033-5b69-3f7e-a29c-132c038b04f6 | -6.213 | -42.4294 | 2025-09-04 12:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 160.4 |
| cdc0c60c-888e-3e81-80a9-11d9cde8b182 | -10.4658 | -50.3907 | 2025-09-04 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 1b387aa6-86ed-3f2e-9c32-af4b6eb289fe | -10.6769 | -51.5767 | 2025-09-04 12:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 9e59df58-62db-3b84-8005-42f7d02638d9 | -5.7 | -45.1786 | 2025-09-04 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 145.8 |
| e6c54741-c29c-39c3-819b-6efce3d62898 | -8.0417 | -45.3882 | 2025-09-04 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 127.1 |
| f57223f0-b6ff-3d18-b154-7628776b784d | -5.6777 | -45.6089 | 2025-09-04 12:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 4c9453a9-b905-3f42-8512-5dd07dde84f1 | -11.8533 | -51.4318 | 2025-09-04 12:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 4f363528-1cc3-3c99-88f4-8a487f93f020 | -5.9441 | -51.9796 | 2025-09-04 12:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0bfc6f3f-6357-3ccb-92b3-254f471a7fec | -11.853 | -51.453 | 2025-09-04 12:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 6a4191f6-8428-3733-80d9-8ebd98829a17 | -6.2318 | -42.4278 | 2025-09-04 12:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 171.6 |
| 11785040-65c6-35e3-86b2-c8a8c23c8792 | -7.6851 | -48.7386 | 2025-09-04 12:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 168.4 |
| a923abf4-f5ef-3c73-81bb-8a16aad51b38 | -9.7108 | -48.9636 | 2025-09-04 12:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 07cd19ce-53e4-3e05-ac42-490690b2e56f | -9.3014 | -47.0986 | 2025-09-04 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 6f3c774f-b91e-3f62-8de9-28a1b00c7724 | -8.0417 | -45.3882 | 2025-09-04 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 9424d8a9-7ded-3fd6-a8fb-8cc5d31fb782 | -11.7389 | -47.7415 | 2025-09-04 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 22fa65e3-19f1-3ad1-ace9-ec39d65c98df | -6.3689 | -45.6483 | 2025-09-04 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 442f5225-86ca-34dd-995c-fd03faeec9a2 | -10.4658 | -50.3907 | 2025-09-04 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 9f55c8aa-5690-3c17-acee-dfdbc34dfadd | -7.3012 | -39.6453 | 2025-09-04 12:30:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 106.1 |
| bb9e57c5-0b08-393f-9ad1-14bf6d5304f5 | -11.7385 | -47.7637 | 2025-09-04 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 2166745f-7d13-3c75-877e-f768c8a1342c | -6.3692 | -45.6258 | 2025-09-04 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 7527f3c8-1cba-3830-a76d-3a49f912d150 | -10.9855 | -49.7562 | 2025-09-04 12:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 92fffa02-5211-3e0b-93d1-2b84d7a1ac71 | -8.3829 | -48.3317 | 2025-09-04 12:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b0e9e29d-6b08-3f09-97d4-8e33937b274e | -8.0228 | -45.39 | 2025-09-04 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| e8ac216f-e778-32f7-9a63-27108309e56e | -7.0502 | -43.2724 | 2025-09-04 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 5950e134-a518-3eb3-b00d-93e6499c204f | -11.6599 | -54.5297 | 2025-09-04 12:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7f653215-4e3a-3403-9c2e-6060c087a0f5 | -13.8457 | -47.9764 | 2025-09-04 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 2debbad2-f7df-35d8-a12e-d98e053a6179 | -6.2315 | -42.4515 | 2025-09-04 12:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 190.7 |
| 9e92b1af-f8d4-3f3d-961a-43c86c0349dd | -8.9031 | -45.82 | 2025-09-04 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| a683dddc-2b53-3e63-b916-a165f5700616 | -4.9049 | -41.7696 | 2025-09-04 12:30:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 140.9 |
| 2303e562-b469-3469-8106-22e0fb8296cf | -8.3641 | -48.3334 | 2025-09-04 12:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e5851b5c-55a7-3147-9ce2-abe51ad8c77c | -10.6769 | -51.5767 | 2025-09-04 12:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| f8322911-3ece-37db-ba5c-9adcaed0f815 | -11.5779 | -52.115 | 2025-09-04 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| cf52f373-4d56-3a20-a806-9ea601b45190 | -13.8651 | -47.9734 | 2025-09-04 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 104.0 |
| d52bb7b9-b0f2-3da1-8fa7-8387f640a994 | -8.0799 | -45.339 | 2025-09-04 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 597bb21b-72df-302c-95a6-0608ff5a9895 | -7.7039 | -48.7371 | 2025-09-04 12:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 990b7026-6b71-307b-815b-3f973d4c040f | -7.6854 | -48.717 | 2025-09-04 12:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 34cf3d23-268f-358d-9e19-f0fc69b313de | -5.7 | -45.1786 | 2025-09-04 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 54689d68-a94f-3d21-975e-811b6afbe7e3 | -6.2127 | -42.4532 | 2025-09-04 12:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| f1e4e320-2643-35ad-bd94-e74f1bae7386 | -6.0421 | -46.6549 | 2025-09-04 12:30:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |


[Clique aqui para ver as próximas entradas](README103.md)
