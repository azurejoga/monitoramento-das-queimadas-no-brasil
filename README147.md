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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2251f679-e81a-3394-a50f-d72da6bfe3ea | -15.8014 | -52.2258 | 2025-09-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 9b74f9ad-4376-3916-b67c-8563358c2183 | -9.9398 | -46.064 | 2025-09-11 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 215.3 |
| 0dc44acc-04c7-3a6a-bd38-d684ac50ca4e | -8.8758 | -49.5399 | 2025-09-11 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 26e60114-b072-348f-a778-42bc5ce51a7b | -6.6652 | -44.1205 | 2025-09-11 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| c8dfb7e1-86dd-3e44-a5c7-e510436c9849 | -10.0695 | -50.3881 | 2025-09-11 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 77f933d4-c1cd-3483-b4c1-986af0673936 | -6.6149 | -45.3807 | 2025-09-11 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 03b97292-1e3d-3113-9eca-c50defd97809 | -9.0942 | -47.076 | 2025-09-11 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 07059358-5f16-3e79-bd71-9a34a7dfa8d5 | -11.4845 | -43.6402 | 2025-09-11 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| bd1565f9-2c7d-3b37-ad2e-80006db17516 | -19.8442 | -45.2529 | 2025-09-11 14:20:00 | GOES-19 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 2c406c03-c1e3-32b0-af6f-f25754a04a37 | -5.7337 | -45.605 | 2025-09-11 14:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 7509fbae-74a8-3ed8-87ef-e28418979f8e | -15.1374 | -52.4039 | 2025-09-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| e7942407-94bc-3810-9930-69f42c71cdd3 | -9.4804 | -46.4321 | 2025-09-11 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| daa86765-ea77-3b20-88fc-b8beb61429d5 | -6.485 | -45.2554 | 2025-09-11 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 8b0158e7-360c-3011-a66f-9461db8eddcf | -9.0265 | -49.5046 | 2025-09-11 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 17a756f1-1425-310a-82fb-678fc686e0ae | -8.3539 | -47.5908 | 2025-09-11 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 3dbc5cad-9a7d-365c-81e9-e12d3dfbacbf | -4.553 | -43.7439 | 2025-09-11 14:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 76c0c0e5-e07f-309d-a15b-744c25b0606c | -6.2228 | -43.3226 | 2025-09-11 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 19adab30-9af2-3f53-9454-94584d9f8b42 | -11.0959 | -51.3443 | 2025-09-11 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 246.0 |
| 15c80a47-6728-3906-a0b4-8557d0b23c00 | -10.7366 | -46.1011 | 2025-09-11 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 85cf5584-d855-349f-8a7c-3cfdaedbdf4c | -15.1759 | -52.4199 | 2025-09-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 711c77e6-adf5-366e-ab21-1316ee90461b | -10.6796 | -48.6196 | 2025-09-11 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| b1109102-f6e9-3d40-889e-110be61b2ec1 | -8.994 | -46.0808 | 2025-09-11 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 1b27acfe-2dbf-36e0-8a26-842e03f87f00 | -11.7211 | -46.5127 | 2025-09-11 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 287.3 |
| a105a781-67ab-3b02-a518-dbc580486c1e | -9.075 | -47.1002 | 2025-09-11 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 9d2028dc-1496-38ae-b030-407c494a00e0 | -6.5962 | -45.3822 | 2025-09-11 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| f8526499-e17a-3d3e-a58b-822c190d6c71 | -9.976 | -50.3334 | 2025-09-11 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 533c07bb-ccb4-3ce3-a3ff-3a08865af645 | -14.4004 | -47.327 | 2025-09-11 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 298a5188-fc20-3300-965b-3982f6efd125 | -11.779 | -46.4821 | 2025-09-11 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 57536544-baf1-383a-8ec4-e6db9d27f83b | -22.6809 | -53.1309 | 2025-09-11 14:20:00 | GOES-19 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 114.9 |
| 350bfdf8-ecec-3a6e-8587-cdecc249286b | -10.203 | -46.213 | 2025-09-11 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 182.9 |
| fb7172ed-4f4e-3ee2-8ef3-a04fa6597ad9 | -11.1685 | -45.3144 | 2025-09-11 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 97d7d40f-2c8a-3be0-aada-72c7e074ed13 | -22.6601 | -53.135 | 2025-09-11 14:20:00 | GOES-19 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 84.8 |
| 46fb9fa7-b214-3af9-9cab-f8e0999fe8a2 | -14.4323 | -52.9408 | 2025-09-11 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 958b3455-ed22-3bbc-b1f8-fdb1ecdff553 | -7.4349 | -45.8519 | 2025-09-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| f774ada8-b987-37d3-b14a-e07a7ea8bf60 | -11.4849 | -43.6166 | 2025-09-11 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 52fc3931-b4ba-32fd-a94d-0c78b69d781d | -19.9994 | -47.6271 | 2025-09-11 14:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 1175c29a-e935-35f6-a7e1-10e096e7cc9c | -9.0565 | -47.08 | 2025-09-11 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 76dec74d-f259-3159-8810-469156e94dd8 | -6.3041 | -53.4562 | 2025-09-11 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 53836b24-1aba-381a-83b9-07d5d8dc67a5 | -12.9292 | -54.7538 | 2025-09-11 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 695dcaf8-8062-3772-b0ff-c44d019820aa | -10.859 | -45.5851 | 2025-09-11 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 20575a2a-dda4-3ca0-8f3d-23c57b7fd2f6 | -15.1557 | -52.4652 | 2025-09-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| f886075d-eba6-3d14-bb21-cd383a0eff33 | -6.1705 | -41.0658 | 2025-09-11 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| e893fa90-ce2a-3ef2-b420-c1ed8d806226 | -6.8525 | -47.8707 | 2025-09-11 14:20:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 75c3ae99-cf7c-3a04-a5d0-73b76ad945e2 | -15.1561 | -52.4439 | 2025-09-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| fbd22416-a3cd-31c1-aee2-fb483c420000 | -11.4836 | -43.6875 | 2025-09-11 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 688c443a-bc70-321b-b7aa-4d044c766e10 | -8.1649 | -46.0983 | 2025-09-11 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 5bbfd37e-554d-3b1d-8800-7410a6f324ac | -7.5215 | -48.2753 | 2025-09-11 14:20:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9e6d8d49-11dd-3386-ab70-c5d09a90ee4a | -10.7557 | -46.0987 | 2025-09-11 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 0e2b3380-4172-3d05-82f2-b35e554ec77c | -10.6606 | -48.6218 | 2025-09-11 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 420a15ac-eedd-3ebe-a115-ddd285bce09b | -10.5671 | -47.2442 | 2025-09-11 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 280.8 |
| 58847e6d-28ea-30f9-b40c-83da48e6d59e | -9.0745 | -45.7109 | 2025-09-11 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 2bd3e781-5756-3dde-b69d-f7ef975d7a9b | -6.3735 | -45.1736 | 2025-09-11 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| e42e3b23-8136-39f1-a495-f5c5c27d2a9d | -11.7786 | -46.5047 | 2025-09-11 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 224.2 |
| fe5b412d-a2b2-3bec-b56d-80dd24cb0df3 | -9.9762 | -50.3121 | 2025-09-11 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 215.2 |
| 0966ede6-1c2d-38f1-be52-a6473d17a3f3 | -17.3366 | -46.6951 | 2025-09-11 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 7e25335c-00a9-3426-9507-986f6b81c7ea | -15.1565 | -52.4226 | 2025-09-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 10d1d384-0e29-3b8e-8a30-cf7cd45d1822 | -15.8006 | -52.2687 | 2025-09-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 184.3 |
| d77f7879-7379-323f-bda7-5e312d1d2ae3 | -6.684 | -44.1189 | 2025-09-11 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 3497f0bc-8a71-385f-b28a-60f6f60dfe98 | -14.2881 | -54.7514 | 2025-09-11 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 16d7b582-f68c-3662-98d4-51c0535af900 | -15.1565 | -52.4226 | 2025-09-11 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d1282098-3ba9-3e11-8421-a06c90f7c9ca | -15.6929 | -47.0354 | 2025-09-11 14:30:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 9b60a906-6842-3ed5-92a8-741f891b53be | -8.8755 | -49.5613 | 2025-09-11 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 687cf5d3-c772-3fbb-a88d-c11d333d952f | -15.5628 | -54.7453 | 2025-09-11 14:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 454ee802-dcc9-38ed-8dc3-3fc1583cd7f6 | -9.9762 | -50.3121 | 2025-09-11 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 233.0 |
| 5b552198-75e9-37e4-8060-a4acbcd7eec6 | -15.1367 | -52.4466 | 2025-09-11 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 513289e7-fe20-3e3a-9b1f-0702507c1d03 | -7.4448 | -44.9678 | 2025-09-11 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 02f601a2-d746-3635-bd75-42fff9d11f15 | -6.8525 | -47.8707 | 2025-09-11 14:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f6a047ab-d051-386a-a7b6-8c558b2c5a5e | -4.553 | -43.7439 | 2025-09-11 14:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| e7716431-aafe-3569-a0c4-3cb62ea21fe4 | -6.6652 | -44.1205 | 2025-09-11 14:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| daa8b182-79a9-36ea-a011-6023c32e8608 | -9.9398 | -46.064 | 2025-09-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| b7a97faf-0f24-3110-9eff-ecbd7faf44a7 | -9.7634 | -47.8447 | 2025-09-11 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 94e70f4d-e409-37f2-a61e-deb18c3c10ac | -7.8998 | -46.2581 | 2025-09-11 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 89dffcbc-60ff-31f2-b7f0-afe9d27dfbae | -7.5215 | -48.2753 | 2025-09-11 14:30:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 0ed84d11-6705-3a87-a994-3abfc6e47d1c | -6.9319 | -45.5352 | 2025-09-11 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 8afdf242-2539-36fb-8bfd-f05dcb78aa22 | -9.0358 | -45.783 | 2025-09-11 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 630728d5-af17-3afb-8906-5c63bdaa7e57 | -15.8201 | -52.2659 | 2025-09-11 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 50446c07-4952-3cda-bcca-a54c2704b4a5 | -6.485 | -45.2554 | 2025-09-11 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| ac949e3e-dbe0-309b-8030-6127f3072a5a | -11.7399 | -46.5326 | 2025-09-11 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 51da6e4e-d0c7-3197-9b14-53fc91d1d53e | -9.0791 | -49.8211 | 2025-09-11 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 63045e0b-41c8-32dc-8ade-04d8bcc031b5 | -9.0753 | -47.078 | 2025-09-11 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 97db5816-78a5-3d20-841e-ec6d1f83361a | -10.3885 | -50.5264 | 2025-09-11 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 197.4 |
| ed181273-5275-328f-b9de-d5d861315343 | -9.9004 | -51.8811 | 2025-09-11 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 5530b647-70d6-3122-8903-db90a3b46d12 | -14.3074 | -54.7492 | 2025-09-11 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| fbc6be00-154f-3a8f-bf45-482ad34b17ac | -9.075 | -47.1002 | 2025-09-11 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| b917d3dc-bf19-32bf-8ba4-e966dfbfd591 | -10.7366 | -46.1011 | 2025-09-11 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 05d1eabf-b320-38b9-a613-2df42978b70e | -6.5038 | -45.2539 | 2025-09-11 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| e369c3b3-e523-3728-9490-bf529cb76fc5 | -11.7211 | -46.5127 | 2025-09-11 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 313.3 |
| f66d010b-21c2-37a6-a2fc-4f711bc2a4b4 | -10.6413 | -48.6458 | 2025-09-11 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 73af93b7-7f7e-33e1-8ce4-0f6fd48845f2 | -8.1649 | -46.0983 | 2025-09-11 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 47b0efbc-4f7e-3fad-a0d8-0ff9c89d20d9 | -14.7334 | -60.2337 | 2025-09-11 14:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 4e4ae7bc-986a-38ca-adfc-570826c57bd5 | -11.4849 | -43.6166 | 2025-09-11 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 2982b190-b694-3a2a-a89e-e770161ab3f3 | -9.1328 | -47.0054 | 2025-09-11 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8afe9d70-e60f-3849-b5ec-d249fe6a9720 | -6.3158 | -43.4081 | 2025-09-11 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 6ec10145-1ed0-35fe-9f6a-7834c4bec2f5 | -6.8374 | -45.6108 | 2025-09-11 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8449b2c9-039a-3da8-aeae-45ae8df09f4c | -12.9292 | -54.7538 | 2025-09-11 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 4fa077d8-d7c1-3991-80b1-2a49f1ba4e86 | -5.6607 | -45.4074 | 2025-09-11 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f684562a-79b4-3a91-8788-6b3f3e8b0bd8 | -14.5006 | -53.4784 | 2025-09-11 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 458f731f-20c2-3d13-8aad-ca07b2e0634b | -11.484 | -43.6639 | 2025-09-11 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 93ff97c5-123e-3f7d-b523-6e16dcab3d16 | -10.8594 | -45.5622 | 2025-09-11 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.3 |
| cf5e02e2-d11a-3697-9bc2-3a6fec4a3d56 | -14.4461 | -53.2755 | 2025-09-11 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |


[Clique aqui para ver as próximas entradas](README148.md)
