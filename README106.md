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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 784323f8-7488-3f9d-b4bf-06e81954bcc7 | -12.2825 | -44.0804 | 2025-09-28 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 354.0 |
| 442934e8-2c32-3c99-9295-8f719942e5d6 | -12.0218 | -47.9481 | 2025-09-28 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| e48d782b-d30a-3ed8-bb03-f8dbde6002ba | -5.7001 | -43.0604 | 2025-09-28 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 5e7e4832-c398-32d6-beee-af9e6c181d15 | -12.791 | -47.7533 | 2025-09-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 321.2 |
| c8817c63-bea1-3d8f-bad2-39731d9d8aa6 | -6.3154 | -43.4548 | 2025-09-28 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| c276fc23-16c8-34e6-84bb-da67d96b4bca | -9.7457 | -47.7586 | 2025-09-28 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 33f71799-659b-362b-b120-5a2fc64814d6 | -11.4083 | -46.9597 | 2025-09-28 14:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 6bb637d9-ff2a-3cd4-ac1f-7de17db46389 | -8.1611 | -46.4122 | 2025-09-28 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 3a8785a5-2191-3dea-a09a-7d8e2c40036a | -7.882 | -44.5824 | 2025-09-28 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 866.3 |
| 62cb779e-dc2b-3d76-8b02-e21ab63726a2 | -10.8242 | -45.3841 | 2025-09-28 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.8 |
| 754964c9-05e3-3ef1-bb13-5eb2cb7c3741 | -14.3816 | -54.9266 | 2025-09-28 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 3129ab20-49d0-3863-bb86-4e666d9c3256 | -5.7583 | -42.8447 | 2025-09-28 14:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 2c1282ca-0e28-3d64-8fb4-aba3583e9336 | -12.0181 | -47.0344 | 2025-09-28 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| bd215bfd-2e1a-3a6d-afe4-846124b05a98 | -11.3654 | -44.9645 | 2025-09-28 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 274.0 |
| 9e845036-b824-38fb-866a-a498b74e021b | -4.1491 | -39.998 | 2025-09-28 14:20:00 | GOES-19 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 37352495-28e4-3493-9121-15c4147b2e79 | -8.1614 | -46.3899 | 2025-09-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| b1dc81e5-e751-37da-b041-31dba39e7326 | -6.5062 | -45.0041 | 2025-09-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 02439aff-e9c1-31cd-b908-c58f0b740570 | -9.4007 | -54.6984 | 2025-09-28 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 223.5 |
| 8bd44837-2da9-39ac-81a8-c7374ec36c5f | -11.979 | -47.0847 | 2025-09-28 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 56a4c786-b922-3359-bad7-0ff81424c295 | -6.2759 | -43.6442 | 2025-09-28 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 74e6e203-7bd4-372a-81bd-ef1732d97086 | -11.3642 | -45.0339 | 2025-09-28 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| addb3d51-544b-3ee0-b08e-bae8ab1fd113 | -11.9644 | -47.9557 | 2025-09-28 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 216.8 |
| ac866f89-9fbd-3c99-9e47-03483eef095d | -13.2969 | -50.6821 | 2025-09-28 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 1a9aef15-c33c-3bc9-a9ab-b389dfc1fa4a | -12.0214 | -47.9703 | 2025-09-28 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b6122033-94e3-3a33-ab2d-09282b0555fe | -13.2781 | -50.663 | 2025-09-28 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 775f15e1-928a-3df9-8f84-ae9711d1fef4 | -8.2665 | -45.4791 | 2025-09-28 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 693179ee-f191-35be-a542-4ef6ef786ebb | -6.3 | -45.0205 | 2025-09-28 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 996f458b-2b44-3dbf-a121-9b2c6f6b98a5 | -12.2829 | -44.0568 | 2025-09-28 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 84a7f0d5-a4c3-3e13-812b-a7788204c0c4 | -10.8238 | -45.407 | 2025-09-28 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.4 |
| a41d83d8-4302-3337-8adf-fb50fa15f27e | -6.6178 | -45.0859 | 2025-09-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| da1a9694-faf9-30f4-9bba-2b9bea9cc2de | -6.6002 | -44.9736 | 2025-09-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 0b9949d7-c836-31c8-8557-962cf7309cd1 | -9.0913 | -45.8673 | 2025-09-28 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 13f4fa1d-ffe2-393e-99ad-dde5b8bb274e | -15.6092 | -53.1669 | 2025-09-28 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| af05e261-561e-3182-82e6-3f5238e73b42 | -14.765 | -45.7086 | 2025-09-28 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 196.8 |
| 7fc62a8f-8d4a-36de-92ac-b881861333d5 | -10.0184 | -48.5401 | 2025-09-28 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 78ef031c-bf06-3201-89aa-3b8c746220c7 | -4.7434 | -43.2679 | 2025-09-28 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| a2b9d866-c05e-3ef4-9022-be77a5d0cdd7 | -9.4009 | -54.6781 | 2025-09-28 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| fd08e12f-4c46-3232-b529-5e371129a80a | -5.6223 | -43.3701 | 2025-09-28 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 26befd00-8ac0-3073-9966-960ac99c7ba8 | -7.8634 | -44.5612 | 2025-09-28 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 144.0 |
| a915e4c2-9fcf-37d4-9e87-6228cfcddcc2 | -8.6798 | -47.0738 | 2025-09-28 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| f2f5353d-a254-371e-8f02-5e100fbfa13b | -11.4237 | -44.9099 | 2025-09-28 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 3fb95161-c4f9-3ac8-96c6-8d331f1b8478 | -5.6461 | -44.933 | 2025-09-28 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 78aecbda-d9ba-3a3c-91f0-477707e55d73 | -8.2856 | -45.4545 | 2025-09-28 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 268.0 |
| a3891bee-321a-3cd4-ae11-08a01e1203c9 | -13.7893 | -47.8957 | 2025-09-28 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 154.4 |
| f1153e8f-91fc-3dc6-b568-7997f6270d7b | -7.3659 | -47.0394 | 2025-09-28 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| d402b67e-8e35-3193-a5ae-1c37d880787c | -7.3849 | -47.0157 | 2025-09-28 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 78cbcd30-3c2c-3288-8ed8-95bf67c85850 | -7.7555 | -45.7324 | 2025-09-28 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 9a30c8c3-01b2-30bb-84e1-8cf50225843a | -6.6192 | -44.9493 | 2025-09-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 40d728d8-77c0-328f-9684-ff99e16fe522 | -9.4192 | -54.7172 | 2025-09-28 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 55022e5c-4ca8-366e-b7ec-328679eaeecb | -5.17 | -43.7276 | 2025-09-28 14:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 081fdd18-bbe2-3091-9b34-18cb334b7c55 | -7.5089 | -44.297 | 2025-09-28 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a2fa099a-297b-3d65-95d8-a71ae58427a4 | -7.8823 | -44.5594 | 2025-09-28 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 344.0 |
| feb122be-67c5-3a81-9f4e-38c2b1f6411d | -13.2966 | -50.7036 | 2025-09-28 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d1175515-39d3-3e82-b574-53f14d14ca8b | -11.9982 | -47.0821 | 2025-09-28 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 720d6275-540a-3aba-9788-5e2429d89586 | -15.8873 | -46.2409 | 2025-09-28 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 945e70be-d0bc-35a1-924c-1dc4ff499eb3 | -11.4409 | -45.0229 | 2025-09-28 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 6fdd9f0b-282b-3eee-8f24-44ffbaaf8794 | -11.9637 | -48.0001 | 2025-09-28 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| a3a6f52e-713b-3ef3-810a-903ff40d6e8f | -5.7396 | -42.8461 | 2025-09-28 14:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 7ac0b15a-7874-3d9c-8eed-d419c0009799 | -6.0625 | -42.4422 | 2025-09-28 14:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| f03c7d0f-5eb4-3eb0-8ccf-966ae6d3213e | -13.2966 | -50.7036 | 2025-09-28 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| f3f1421c-2e6b-32a3-bdd8-c5e13e021abd | -7.1571 | -45.5158 | 2025-09-28 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 9e11472a-6e22-3db2-9112-3075101d8930 | -6.6002 | -44.9736 | 2025-09-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 6f19949f-b99e-34f8-aff6-3c1d1fed2f76 | -10.9923 | -45.5901 | 2025-09-28 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| e63364be-e41f-30b9-935d-b7494bcc2e0c | -11.964 | -47.9779 | 2025-09-28 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 90ab3365-d11e-3ae3-8d98-972ce1a89c1f | -11.9824 | -48.0197 | 2025-09-28 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 904227be-5933-3c18-8c14-2f60e61a24bb | -5.6461 | -44.933 | 2025-09-28 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| de0c869c-ee98-3176-bc7f-170ee5935b7a | -13.7704 | -47.8763 | 2025-09-28 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 90981fb8-dfe5-34f2-a439-2bc61180f3ac | -10.9736 | -45.5698 | 2025-09-28 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 9b581cb1-46b8-3fb5-aa01-8c2964ba8e7a | -12.0214 | -47.9703 | 2025-09-28 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| dc9b4566-eb6a-3399-a03b-407f3f2de945 | -14.576 | -48.2417 | 2025-09-28 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 6def8a4e-7042-3fe0-9a1a-10c9dd2dc93b | -8.1614 | -46.3899 | 2025-09-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| e1ff925a-7e27-3d95-9bf8-0e716aa08fb4 | -7.3661 | -47.0173 | 2025-09-28 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 183f20d6-d809-3ed1-b19c-31fb37b0e91a | -12.0222 | -47.9259 | 2025-09-28 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| d0ed391f-0a75-3779-8a9a-0361e0a34d3a | -9.106 | -47.6275 | 2025-09-28 14:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f12b0c77-def8-36c5-98e1-4efeafd02681 | -9.0913 | -45.8673 | 2025-09-28 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 82c2cae7-fc79-3856-9043-14bd866ac3c9 | -13.7889 | -47.9181 | 2025-09-28 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 5d425dfa-022b-31d9-9745-a56c3b18e1d1 | -9.9581 | -43.5987 | 2025-09-28 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| b618f675-9a25-31c5-9673-67fdfbc00825 | -9.7643 | -47.7786 | 2025-09-28 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 3ef23e54-c9a7-30a4-a0ed-3d7528ad693f | -6.6005 | -44.9509 | 2025-09-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 7ba6afbe-f8e5-3cd7-8d4f-d9d893960b63 | -7.1574 | -45.4932 | 2025-09-28 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ea5236da-1712-339e-97de-e5b62a7c21e3 | -12.8972 | -45.1479 | 2025-09-28 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 315.3 |
| 275c72c2-3beb-3274-a74a-15cccff97591 | -12.4167 | -44.1057 | 2025-09-28 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 76456ee7-5256-33e1-b0ce-f444bb99298b | -12.791 | -47.7533 | 2025-09-28 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 015490bf-a13a-3162-a992-b8ec59feea43 | -10.9927 | -45.5673 | 2025-09-28 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 6faa5c1b-44db-3370-862a-e90effd52872 | -5.2869 | -43.1613 | 2025-09-28 14:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f8e2c148-604a-3ec1-87c5-ff4b8ae1a075 | -8.6798 | -47.0738 | 2025-09-28 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 239.5 |
| 4387fc8a-67c3-3944-a7cb-2bf90843f1ca | -13.6267 | -47.3152 | 2025-09-28 14:30:00 | GOES-19 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e2c47b19-2958-3925-863e-26991ac3863f | -9.4007 | -54.6984 | 2025-09-28 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 420.9 |
| f4174769-39da-307f-a423-05363e023c40 | -6.0813 | -42.4407 | 2025-09-28 14:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 48690a9a-2eeb-34b8-b4ef-f1898bb91045 | -6.3105 | -45.8999 | 2025-09-28 14:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 609abff3-87ec-3f0f-8712-8c465aef3b2a | -8.8759 | -45.0274 | 2025-09-28 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 192.0 |
| e4fffac9-5ab4-31ef-ad7a-b247ad2a426f | -8.2419 | -47.5352 | 2025-09-28 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4e4c13a6-4502-33ab-abe1-8eaba2458b55 | -11.4237 | -44.9099 | 2025-09-28 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b8c058aa-11ef-3be9-8427-be213d6137a1 | -11.3846 | -44.9618 | 2025-09-28 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| d71dfbb4-5467-38eb-b3d8-14b2928401cf | -11.4217 | -45.0257 | 2025-09-28 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 15c59165-5160-3abc-ae62-4c5a8e14b161 | -12.2825 | -44.0804 | 2025-09-28 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| b83b98bc-5407-3e60-9f43-db8c1894cc8b | -15.6092 | -53.1669 | 2025-09-28 14:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 2010f8a2-0f24-3e9c-90d7-2b0b7544805f | -5.9072 | -45.005 | 2025-09-28 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| f4355060-898e-3949-960f-268cfbcca3f7 | -8.6442 | -43.9931 | 2025-09-28 14:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 0ef4de0d-b842-3674-b063-e9407a59b0f4 | -7.8823 | -44.5594 | 2025-09-28 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 223.8 |


[Clique aqui para ver as próximas entradas](README107.md)
